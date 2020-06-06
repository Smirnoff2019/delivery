from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework import serializers
from market.models import Consumer


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ('id', 'name', 'phone', 'address', 'geo_location')


class ConsumerListView(ListModelMixin, GenericAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer

    # filterset_class = ConsumerFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


from rest_framework import viewsets
from rest_framework import permissions


class ConsumerViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to read and modify consamers.
    """
    queryset = Consumer.objects.all().order_by('-id')
    serializer_class = ConsumerSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'get', 'put', 'patch', 'delete']