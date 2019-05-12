from rest_framework import serializers
from .models import Contact
from django.contrib.auth import authenticate


# Contact Serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'listing', 'listing_id',
                  'name', 'email', 'phone', 'message', 'user_id')

    def create(self, validated_data):
        listing = validated_data['listing']
        listing_id = validated_data['listing_id']
        name = validated_data['name']
        email = validated_data['email']
        phone = validated_data['phone']
        message = validated_data['message'] if 'message' in validated_data else ''
        user_id = validated_data['user_id']

        # if request.user.is_authenticated:
        #   user_id = request.user.id
        #   has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        #   if has_contacted:
        #     messages.error(request, 'You have already made an inquiry for this listing')
        #     return redirect('/listings/'+listing_id)
        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        return contact
