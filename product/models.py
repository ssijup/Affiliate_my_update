from django.db import models
import uuid

from userapp.models import UserData

LINK_HOLEDR_ROLE_CHOICE = {
    ('influencer' ,'influencer'),
    ('organiser' ,'organiser'),
    ('admin', 'admin')
}

class Product(models.Model):
    name = models.CharField(max_length =250)
    description = models.TextField()
    subcription_fee = models.CharField(max_length = 10)
    created_by = models.ForeignKey(UserData, on_delete = models.CASCADE,default = '1')
    unique_id = models.CharField(max_length = 15,null = True, blank= True, unique= True)
    product_link = models.URLField(blank=True, null=True)  # Use URLField for storing links


class RegionData(models.Model):
    user = models.ForeignKey(UserData, on_delete= models.CASCADE)


class RefferalLink(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(UserData, on_delete = models.CASCADE, related_name = 'link_generator')# the link generator ie the perosn got is registering
    direct_referred_link_owner = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name='direct_referred_links', null=True)#ie influner
    indirect_referred_link_owner = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name='indirect_referred_links', null=True)#ie organiser
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    link_holder_role = models.CharField(max_length=50, choices=LINK_HOLEDR_ROLE_CHOICE, default='admin')
    created_at = models.DateTimeField(auto_now_add=True)
    # generated_by = models.ForeignKey(UserData, on_delete = models.CASCADE)


class Payment(models.Model):
    user = models.ForeignKey(UserData, on_delete= models.CASCADE)










