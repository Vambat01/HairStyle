from rest_framework import pagination
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import status

from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10
    pagination_class.max_limit = 100

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        profile = request.data
        serializer = ProfileSerializer(data=profile)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetail(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10
    pagination_class.max_limit = 100

    def get(self, request, pk):
        profile = get_object_or_404(Profile, name=pk)
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        print(2)
        saved_profile = get_object_or_404(Profile, name=pk)
        data = request.data
        serializer = ProfileSerializer(instance=saved_profile, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        profile = get_object_or_404(Profile, name=pk)
        profile.delete()
        return Response({
            "message": "Profile with id {} has been deleted.".format(pk)
        }, status=status.HTTP_200_OK)

class ProfileOrderList(generics.ListAPIView):
#class ProfileDetail(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10
    pagination_class.max_limit = 100

    def get(self, request, pk):
        profile = get_object_or_404(Profile, name=pk)
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        print(2)
        saved_profile = get_object_or_404(Profile, name=pk)
        data = request.data
        serializer = ProfileSerializer(instance=saved_profile, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        profile = get_object_or_404(Profile, name=pk)
        profile.delete()
        return Response({
            "message": "Profile with id {} has been deleted.".format(pk)
        }, status=status.HTTP_200_OK)
 #   serializer = ProfileOrderList
  #  model = Order
   # def get_queryset(self):
    #    user = self.request.user
     #   return super().get_queryset()


