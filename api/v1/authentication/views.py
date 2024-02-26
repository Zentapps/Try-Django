

from rest_framework_simplejwt.views import TokenObtainPairView

from api.v1.authentication.serializers import UserTokenObtainPairSerializer
from posts.models import Post


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

class Login(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer


from urllib import request
from rest_framework import permissions, status, viewsets, mixins
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import APIException, NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from .serializers import PostSerializer, UserSerializer
User = get_user_model()
from rest_framework.generics import  GenericAPIView



class RegisterView(GenericAPIView):

    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.validated_data.pop('password2')
        User.objects.create_user(**serializer.validated_data)

        #TODO : for data preview  update serializer.validated_data with password2
        response_data = {"success": "User Account successfully created."}
        return Response(response_data, status=status.HTTP_201_CREATED)


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_deleted=False)
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.action in ['list', 'retrieve']:
            queryset = queryset.filter(creator=self.request.user)
        return queryset
