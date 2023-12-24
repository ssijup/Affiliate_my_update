from .serializer import CustomTokenObtainPairSerializer, UserDetailsSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from django.db import transaction

from userapp.serializer import UserDataSerializer,UserDetailsSerializer
from product.serializer import ProductSeriaizer,RefferalLinkSerializer, UserRequestingforUpgradingToOrganiserSerializer 
from .models import UserData,UserDetails, UserRequestingforUpgradingToOrganiser
from product.models import Product, RefferalLink
from affiliate.settings import SITE_DOMAIN_NAME


# Create your views here.

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserRegisration(APIView):
    # product_unique_id : will get the product_unique_id from the url of the registration link
    def post(self, request,product_unique_id):
        try:
            with transaction.atomic():

                data = request.data
                name = request.data.get('name')
                email = request.data.get('email')
                password = request.data.get('password')
                # product_unique_id = request.data.get('product_unique_id')#will get it from the 
                if UserData.objects.filter(email = email).exists():
                    return Response({'message' : 'This email alredy exists .Try another one'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    try:
                        product = Product.objects.get(unique_id = product_unique_id)
                    except Product.DoesNotExist:
                        return Response({'message' : '1Something when wrong.. Please try again later'})
                    user = UserData.objects.create_user(name = name, email = email,  password=password)
                    data['user_id'] = user.id
                    print(user.name,'kl')
                    user_details_serializer =UserDetailsSerializer(data = data)
                    if user_details_serializer.is_valid():
                        user_uuid = user.uuid
                        role_hoding = 'influencer'
                        link = f'{SITE_DOMAIN_NAME}/association/{role_hoding}/linkactivation/{product_unique_id}/{user.name}/{user_uuid}'
                        user_link =user_details_serializer.save()
                        user_link.user_refferal_link = link
                        user_link.save()
                        data['user_id'] = user.id
                        data ['product_id'] = product.id
                        data['link_holder_role'] = 'influencer'
                        link_serializer = RefferalLinkSerializer(data=data)
                        if link_serializer.is_valid():
                            link_serializer.save()
                        return Response({'link_data' : link_serializer.data,'userdetails_data' : user_details_serializer.data,'message' : "Your registration is successful.Please login Now"},status=status.HTTP_200_OK)
                    print(user_details_serializer.errors)
                    # user.delete()
                    return Response({'message' : "Please check the entered details"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'message' : 'Someting whent wrong...Please try again'},status=status.HTTP_400_BAD_REQUEST)


#To get the user details once they logged in
class GetUserDetails(APIView):
    def get(self, request):
        user =request.user
        user_data = UserData.objects.get(id = user.id)
        try :
            details = UserDetails.objects.get(user = user_data)
            serializer = UserDetailsSerializer(details)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except UserDetails.DoesNotExist:
            return Response({'message' : "Something when wrong please try again"},status=status.HTTP_400_BAD_REQUEST)


class UserRequestingAdminforUpgradeToOrganiser(APIView):
    def post(self,request):
        try:
            user = request.user
            user_data = UserData.objects.get(id = user.id)
            user_refferal_link = RefferalLink.objects.get(user = user_data)
            data = request.data
            data['user_id']= user.id
            data['ref_link_id'] = user_refferal_link.id
            user_up_serializer = UserRequestingforUpgradingToOrganiserSerializer(data =user_refferal_link)
            if user_up_serializer.is_valid():
                user_up_serializer.save()
                return Response({'message' : 'Your request for upgrading to organiser leve submmited sucessfully', 'data' : user_up_serializer}, status=status.HTTP_201_CREATED)
            return Response({'message' : "Something when wrong please try again"},status=status.HTTP_400_BAD_REQUEST)
        except UserData.DoesNotExist:
            return Response({'message' : "Something when wrong please try again"},status=status.HTTP_400_BAD_REQUEST)
        except RefferalLink.DoesNotExist:
            return Response({'message' : "Something when wrong please try again"},status=status.HTTP_400_BAD_REQUEST)


#to get the user request for upgradation in the admin dashboard
class GetUSerUpgradationRequests(APIView):
    def get(self, request):
        users = UserRequestingforUpgradingToOrganiser.objects.all()
        serializer = UserRequestingforUpgradingToOrganiserSerializer(users, many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)



#To approve or reject user request to upgradation
class UserResquestApproValForUpgradation(APIView):
    def patch(self,request,upgrading_user_id):
        pass


#
class CreateProductClicksForUser(APIView):
    def patch(self, request, product_unique_id,link_uuid):
        try:
            link = RefferalLink.objects.get(uuid = link_uuid, product__unique_id = product_unique_id)
            link.clicks = +1
            link.save()
            return Response({'message' : 'link of user clicked'}, status=status.HTTP_201_CREATED)
        except RefferalLink.DoesNotExist:
            return Response({'message' : "Something whent wrong...Please try again later"})


#To displaying the details of a user when clicked     
class DetailsOfUserUsingId(APIView):
    def get(self, request, user_id):
        try:
            user = UserData.objects.get(id = user_id) 
            user_details = RefferalLink.objects.filter(user = user)
            serializer = RefferalLinkSerializer(user_details, many = True)
            return Response(status= status.HTTP_200_OK)
        except UserData.DoesNotExist:
            return Response({'message' : "Something whent wrong...Please try again later"})
        
#Done api in excel ^^
