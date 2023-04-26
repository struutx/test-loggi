from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from .models import User
from .serializers import UserSerializer


class ListUsers(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetails(APIView):
    """
    View to handle CRUD operations
    """

    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def get(self, request, user_id, *args, **kwargs):
        user = self.get_object(user_id)

        if not user:
            return Response({'User not found!'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserCreate(APIView):
    def post(self, request, *args, **kwargs):
        content = dict(name=request.data.get('name'), email=request.data.get('email'))
        serializer = UserSerializer(data=content)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateUser(APIView):
    def put(self, request):
        try:
            user_id = request.data.get('user_id')
            to_update_email = request.data.get('email')

            if not user_id or not to_update_email:
                return Response(False, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.get(id=user_id)

            user.email = request.data.get('email')
            user.save()

            return Response(True, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(False, status=status.HTTP_404_NOT_FOUND)


class DeleteUser(APIView):
    def delete(self, request, user_id, *args, **kwargs):
        try:
            user = User.objects.get(pk=user_id)

            user.delete()

            return Response({'User deleted!'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'User not found!'}, status=status.HTTP_404_NOT_FOUND)



