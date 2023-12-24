from rest_framework import serializers


from .models import Product,RefferalLink,RegionData,Payment
from userapp.models import UserData
from userapp.serializer import UserDataSerializer, UserRequestingforUpgradingToOrganiser


class ProductSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RefferalLinkSerializer(serializers.ModelSerializer):
    product = ProductSeriaizer(read_only=True)
    user = UserDataSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all(), source='product')   
    user_id = serializers.PrimaryKeyRelatedField(write_only = True, queryset=UserData.objects.all(), source='user')
    class Meta:
        model = RefferalLink
        fields = '__all__'


class UserRequestingforUpgradingToOrganiserSerializer(serializers.ModelSerializer):
    user = UserDataSerializer(read_only=True)
    user_refferal_link = RefferalLinkSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=UserData.objects.all(), source='user')
    ref_link_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=RefferalLink.objects.all(), source='user_refferal_link')
    class Meta:
        model = UserRequestingforUpgradingToOrganiser
        fields = '__all__'


