from django.urls import path
from .views import (CreateProductView,CreateProductClicks,GetAllProductDeatilsInAdminDash)

urlpatterns = [
    #To create a product in  admin side 
    path('create',CreateProductView.as_view(), name = 'CreateProductView'),

#Done in excel ^
    #To create ie increce prodct link clicked  count
    path('link/clicked/<product_unique_id>',CreateProductClicks.as_view(), name = 'CreateProductClicks'),
    #To get all the product and its details in the admin side
    path('details/list',GetAllProductDeatilsInAdminDash.as_view(), name = 'GetAllProductDeatilsInAdminDash'),


    

]
