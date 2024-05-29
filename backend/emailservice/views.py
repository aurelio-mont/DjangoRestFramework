from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from email.message import EmailMessage
from cfehome.settings import EMAIL_SERVICE

import ssl
import smtplib

class EmailAPIView(APIView):
    def post(self, request):
        try:
            email_from = EMAIL_SERVICE.get("EMAIL_FROM")
            email_password = EMAIL_SERVICE.get("EMAIL_PASSWORD")
            email_smtp_server = EMAIL_SERVICE.get("EMAIL_SMTP_SERVER")
            email_port_server = EMAIL_SERVICE.get("EMAIL_PORT_SERVER") 

            email_to = request.data['to_email']
            email_subject = request.data['subject']
            email_content = request.data['message']

            email_message = EmailMessage()
            email_message['Subject'] = email_subject
            email_message['From'] = email_from
            email_message['To'] = email_to
            email_message.set_content(email_content)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(email_smtp_server, email_port_server, context=context) as SMTP:
                SMTP.login(email_from, email_password)
                SMTP.sendmail(email_from, email_to, email_message.as_string())

            return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
email_api_view = EmailAPIView.as_view()