from cgitb import lookup
from datetime import datetime
from django.db.models import Q
from django.utils.text import slugify

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.models import Clinic,Department,Role,User
from users.serializers import UserSerializer, LoginUserSerializer

class RegistrationAPI(generics.GenericAPIView):
    permission_classes = (permissions.IsAdminUser, )

    def post(self, request, *args, **kwargs):
        data = request.data

        user = User.objects.create(
            name = data.get('name'),
            email = data.get('email'),
            username = data.get('email'),
            staff_id = data.get('staff_id'),
            clinc = data.get('clinc'),
            department = data.get('department'),
            role = data.get('role'),
            phone = data.get('phone'),
            birthday = data.get('birthday'),
            staff_code = data.get('staff_code'),
            gender = data.get('gender'),
            resigned_at = data.get('resigned_at'),
            nickname = data.get('nickname'),
            probation_till = data.get('probation_till'),
            is_staff = False
        )

        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class UpdateUserAPI(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'uuid'

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data

        if request.data.get('nickname'):
            user.nickname = request.data.get('nickname')
        if request.data.get('department'):
            user.department = request.data.get('department')
        if request.data.get('role'):
            user.role = request.data.get('role')
        if request.data.get('clinic'):
            user.clinuc = request.data.get('clinic')
        if request.data.get('salary_type'):
            user.salary_type = request.data.get('salary_type')
        if request.data.get('salary_amount'):
            user.salary_amount = request.data.get('salary_amount')
        if request.data.get('have_OT'):
            user.have_OT = request.data.get('have_OT')
        if request.data.get('ate_OT'):
            user.rate_OT = request.data.get('rate_OT')
        if request.data.get('annualLeave'):
             user.annualLeave = request.data.get('annualLeave')
        if request.data.get('resigned_at'):
            user.resigned_at = request.data.get('resigned_at')
        if request.data.get('trail_till'):
            user.trail_till = request.data.get('trail_till')
        if request.data.get('is_active'):
            if not request.data.get('is_active'):
                user.is_active = False
            else:
                user.is_active = True
        
        user.save()
        token, _ = Token.objects.get_or_create(user=user)

        data = {
            'user':self.get_serializer(user).data,
            'token':token.key
        }

        return Response(data, status=status.HTTP_200_OK)

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(deta=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        token,_ = Token.objects.get_or_create(user=user)

        return Response({
            'user':UserSerializer(user).data,
            'token':token.key
        },status = status.HTTP_200_OK)


