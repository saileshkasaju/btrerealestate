from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .serializers import RealtorSerializer
from .models import Realtor


# Realtor Viewset
class RealtorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Realtor.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RealtorSerializer

    def list(self, request):
        queryset = Realtor.objects.all()

        # IsMVP
        is_mvp = request.GET and (
            'is_mvp' in request.GET) and request.GET['is_mvp']
        if is_mvp:
            queryset = queryset.filter(is_mvp=True)

        serializer = RealtorSerializer(queryset, many=True)
        return Response(serializer.data)
