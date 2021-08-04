from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TestJWTView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'JWT Token validated successfully.'}
        return Response(content)