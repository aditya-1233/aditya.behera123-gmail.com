from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from demoapp.serializers import NameSerializer
from rest_framework.viewsets import ViewSet


# Create your views here.
class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        color = ['Red', 'Yellow', 'Green', 'Black']
        return Response({'msg': "Hello Good Morning", 'color': color})

    def post(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = "Hello {}, Good to see you!!!".format(name)
            return Response({'msg': msg})
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        return Response({'msg': 'This is the put method response'})

    def patch(self, request, *args, **kwargs):
        return Response({'msg': 'This is the patch method response'})

    def delete(self, request, *args, **kwargs):
        return Response({'msg': 'This is the delete method response'})


class TestViewSet(ViewSet):
    def list(self, request):
        color = ['Red', 'Yellow', 'Green', 'Black']
        return Response({'msg': "Hello Good Morning", 'color': color})

    def create(self, request):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get("name")
            msg = f"Hello {name}, this is the example of viewset"
            return Response({'msg': msg})
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        return Response({'msg': 'This is the retrieve method response'})

    def update(self, request, pk=None):
        return Response({'msg': 'This is the update method response'})

    def partial_update(self, request, pk=None):
        return Response({'msg': 'This is the partial_update method response'})

    def destroy(self, request, pk=None):
        return Response({'msg': 'This is the Destroy method response'})
