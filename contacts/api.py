from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import ContactSerializer


# Inquiry API
class InquiryAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user_id'] = 0
        if request.user.id:
            data['user_id'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": 'Inquirey submitted successfully',
        })
