"""View module for handling requests about emails"""
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from tlcapi.models import Email


class EmailView(ViewSet):
    """TLC Emails"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized email instance
        """
        email = Email()
        email.name = request.data["name"]
        email.email = request.data["email"]
        email.phone_number = request.data["phoneNumber"]
        email.message = request.data["message"]
        email.design = request.data["design"]
        email.installation = request.data["installation"]
        email.maintenance = request.data["maintenance"]
        email.hardscaping = request.data["hardscaping"]
        email.sod = request.data["sod"]
        email.leaf_removal = request.data["leafRemoval"]
        email.pots = request.data["pots"]

        try:
            email.save()
            name = email.name
            text = email.message
            number = email.phone_number
            message = [name, text, number, email.design,
                       email.installation, email.maintenance, email.hardscaping, email.sod,
                       email.leaf_removal, email.pots]
            email = email.email
            send_mail(
                'Website Email Request', message, email,
                ['kylieanyce@gmail.com']
            )
            serializer = EmailSerializer(email, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
