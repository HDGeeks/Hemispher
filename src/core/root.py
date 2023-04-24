from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'create-new-user': reverse('users-list', request=request, format=format),
        #'djoser-users': reverse('djoser-users-list', request=request, format=format),
        'sign-in': reverse('sign-in', request=request, format=format),
        'token_obtain_pair': reverse('token_obtain_pair', request=request, format=format),
        'token_refresh': reverse('token_refresh', request=request, format=format),
        'token_verify': reverse('token_verify', request=request, format=format),
        'customers': reverse('customers-list', request=request, format=format),
        'projects': reverse('projects-list', request=request, format=format),
        'surveys': reverse('surveys-list', request=request, format=format),
        'questions': reverse('questions-list', request=request, format=format),
        'answers': reverse('answers-list', request=request, format=format),

       
    })