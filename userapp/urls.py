from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .views import (GetUserDetails, CustomTokenObtainPairView,UserRegisration,UserRequestingAdminforUpgradeToOrganiser,
                    GetUSerUpgradationRequests,DetailsOfUserUsingId, UserResquestApproValForUpgradation,
                      CreateProductClicksForUser)


urlpatterns = [

    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #USER
    #To register a user
    path('user/registration/<product_unique_id>', UserRegisration.as_view(), name='UserRegisration'),
    #To get the user details  logged user after login
    path('single/user/dashboard/details', GetUserDetails.as_view(), name='GetUserDetails'),
    #user request for level upgradation ie from influncer to organiser
    path('user/upgrdation/request', UserRequestingAdminforUpgradeToOrganiser.as_view(), name='UserRequestingAdminforUpgradeToOrganiser'),
    #To get the user request for upgradation in the admin dashboard
    path('user/upgrdation/request/in/admin', GetUSerUpgradationRequests.as_view(), name='GetUSerUpgradationRequests'),

#Done in excel ^
    #To approve or reject user request to upgradation
    path('user/upgrdation/request/approval', UserResquestApproValForUpgradation.as_view(), name='UserResquestApproValForUpgradation'),
    #To increase click count of a particular user  ie the influncer or oraganiser link
    path('user/link/clicked/<product_unique_i>/<link_uuid>', CreateProductClicksForUser.as_view(), name='CreateProductClicksForUser'),
    #To displaying the details of a user when clicked     
    path('user/details/<user_id>', DetailsOfUserUsingId.as_view(), name='DetailsOfUserUsingId'),






    
]
