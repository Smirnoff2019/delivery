from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework import serializers
from market.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name', 'phone', 'rating')


class ProviderListView(ListModelMixin, GenericAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    # filterset_class = ProviderFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


from rest_framework import viewsets
from rest_framework import permissions


class ProviderViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to read and modify consamers.
    """
    queryset = Provider.objects.all().order_by('-id')
    serializer_class = ProviderSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'get', 'put', 'patch', 'delete']