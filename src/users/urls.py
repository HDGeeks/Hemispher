from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)

from users.views import CreateUserView,SignIn

# define all urls related to the users app
router = routers.DefaultRouter(trailing_slash=False)

router.register(r"create-new-user",CreateUserView ,basename ="users")
router.register(r"sign-in",SignIn,basename = "sign-in")


urlpatterns = [
    #path('create/', CreateUserView , name='create-user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]
from rest_framework import routers





urlpatterns += router.urls
