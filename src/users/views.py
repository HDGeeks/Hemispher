from rest_framework import permissions,status
from django.contrib.auth import authenticate
from rest_framework.decorators import action ,api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import ExtendedUser,Role
from rest_framework_simplejwt.tokens import RefreshToken

class CreateUserView(ModelViewSet):
    queryset = ExtendedUser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]





@api_view(['post'])
def signin(request):
    email = request.data['email']
    password = request.data['password']
    
    if not email or not password:
        return Response({"detail": "All required fields must be input"}, status=status.HTTP_400_BAD_REQUEST)
    
    # checkAdminRole = Role.objects.filter(role='Admin')
    # if not checkAdminRole.exists():
    #     return Response({"detail": "Admin role does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request=request, email=email, password=password)
    
    if not user:
        return Response({"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
    
    refresh = RefreshToken.for_user(user)
    
    return Response({
        'detail': 'Successfully logged in',
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'email': user.email
    }, status=status.HTTP_200_OK)