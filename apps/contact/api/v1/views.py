from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .serializers import ContactSerializer
from ...models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    # http://127.0.0.1:8000/api/contact/v1/contacts/<id>/
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']


