from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .views import (GetUserDetails, CustomTokenObtainPairView,UserRegisration,UserRequestingAdminforUpgradeToOrganiser,
                    GetUSerUpgradationRequests)


urlpatterns = [

    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #USER
    #To register a user
    path('user/registration/<product_unique_id>', UserRegisration.as_view(), name='UserRegisration'),
    #To get the user details once they logged in
    path('single/user/dashboard/details', GetUserDetails.as_view(), name='GetUserDetails'),
    #user request for leve upgradation ie from influncer to organiser
    path('user/upgrdation/request', UserRequestingAdminforUpgradeToOrganiser.as_view(), name='UserRequestingAdminforUpgradeToOrganiser'),
    #To get the user request for upgradation in the admin dashboard
    path('user/upgrdation/request/in/admin', GetUSerUpgradationRequests.as_view(), name='GetUSerUpgradationRequests'),


    
]
