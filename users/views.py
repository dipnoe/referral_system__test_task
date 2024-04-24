from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from users.serializers import UserSerializer, UserRetrieveSerializer, VerifySerializer
from users.services import send_auth_code, create_invite_code


class UserAuthAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phone_number = request.data['phone_number']
            user, created = User.objects.update_or_create(
                phone_number=phone_number,
                defaults={'auth_code': send_auth_code()}
            )
            return Response({'user_id': user.id,
                             'phone_number': str(user.phone_number),
                             'auth_code': user.auth_code})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserVerifyAPIView(APIView):
    def post(self, request):
        serializer = VerifySerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            if not user.personal_invite_code:
                user.personal_invite_code = create_invite_code()
                user.auth_code = None
                user.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'personal_invite_code': user.personal_invite_code,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAddInvitedCodeAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        invited_by_code = request.data['invited_by_code']
        User.objects.get(personal_invite_code=invited_by_code)
        user = request.user
        if user.invited_by_code is not None:
            return Response({'message': f'Already invited by {user.phone_number}'},
                            status=status.HTTP_400_BAD_REQUEST)
        if invited_by_code == user.personal_invite_code:
            return Response({'message': 'You cannot use your own code to invite yourself!'},
                            status=status.HTTP_400_BAD_REQUEST)
        user.invited_by_code = invited_by_code
        user.save()
        return Response({"message": "Code successfully activated!"},
                        status=status.HTTP_200_OK)


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserRetrieveSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
