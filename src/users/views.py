from rest_framework import permissions,status
from django.contrib.auth import authenticate
from rest_framework.decorators import action ,api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import ExtendedUser
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from djoser.serializers import UserCreateSerializer

from django.contrib.auth.hashers import make_password

class CreateUserView(ModelViewSet):
    queryset = ExtendedUser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # hash the password before saving the user
        data = request.data.copy()
     
        # hash the password before saving the user
        password = data.get('password')
        hashed_password = make_password(password)
        data['password'] = hashed_password
        
        # create the user object
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # get the email and unhashed password from the request data
        email = data.get('email')
        password = password
        response_data = serializer.data.copy()
        response_body={"Message":"User created successfully",
                       "Email":email,
                       "Password":password}
        # return the response
        headers = self.get_success_headers(serializer.data)
        return Response(response_body, status=status.HTTP_201_CREATED, headers=headers)
    
    # def perform_create(self, serializer):
    #     # hash the password before saving the user
    #     password = serializer.validated_data.get('password')
    #     hashed_password = make_password(password)
    #     serializer.validated_data['password'] = hashed_password
    #     serializer.save()
       
        




@api_view(['post'])
def signin(request):
    
    username = request.data['email']
    password = request.data['password']
    print(username,password)
    if not username or not password:
        return Response({"detail": "All required fields must be input"}, status=status.HTTP_400_BAD_REQUEST)
    
    # checkAdminRole = Role.objects.filter(role='Admin')
    # if not checkAdminRole.exists():
    #     return Response({"detail": "Admin role does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request=request,username=username, password=password)
    print('=====================================>' ,user)
    
    if not user:
        return Response({"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
   
    refresh = RefreshToken.for_user(user)
    print(refresh)
    
    return Response({
        'detail': 'Successfully logged in',
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'email': user.get_username()
    }, status=status.HTTP_200_OK)