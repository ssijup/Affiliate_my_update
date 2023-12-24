from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import random
import string




from .models import Product,RefferalLink,RegionData,Payment
from .serializer import ProductSeriaizer,RefferalLinkSerializer
from userapp.models import UserData
from affiliate.settings import SITE_DOMAIN_NAME





# class CreateProductView(APIView):


class CreateProductView(APIView):

    def generate_unique_id(self):
        characters = string.ascii_letters + string.digits
        unique_id = ''.join(random.choices(characters, k=12))
        print(unique_id)
        return unique_id

    # ... rest of the code ...

    
    def post(self, request):
        user = request.user
        try:
            user_data = UserData.objects.get(id=user.id)
            data = request.data
            product_serializer = ProductSeriaizer(data=data)
            unique_product_id = self.generate_unique_id()
            while Product.objects.filter(unique_id=unique_product_id).exists():
                unique_product_id = self.generate_unique_id()
            data['unique_id'] = unique_product_id
            data['user_id'] = user_data.id
            if product_serializer.is_valid():
                product = product_serializer.save()
                link = f'{SITE_DOMAIN_NAME}/association/linkactivation/{product.unique_id}'
                product.product_link = link
                product.save()
                product = Product.objects.get(unique_id=unique_product_id)
                data['product_id'] = product.id
                data['link_generated_by_id'] = user_data.id
                # creating the link
                link_serializer = RefferalLinkSerializer(data=data)
                if link_serializer.is_valid():
                    link_serializer.save()

                    # generate the link here
                    return Response({'message': 'Product created successfully','link_data' :link_serializer.data, 'product_data': product_serializer.data}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'message': 'Failed: Link generation failed', 'errors': link_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Enter valid details', 'errors': product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except UserData.DoesNotExist:
            return Response({'message': 'Something went wrong. Please try again later.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': 'Something went wrong. Please try again later.', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



