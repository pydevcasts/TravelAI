from django.http import HttpResponseRedirect
from rest_framework.viewsets import ModelViewSet
from contactus.forms import ContactusForm
from contactus.models import Contactus
from contactus.serializers import ContactusSerializer
from django.core.mail import send_mail
from django.contrib import messages
from rest_framework.permissions import AllowAny
# Create your views here.


class ContactusViewSet(ModelViewSet):
    queryset = Contactus.objects.all()
    serializer_class = ContactusSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        if request.method == "POST":
            form = ContactusForm(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data["name"]
                message = form.cleaned_data["message"]
                email = form.cleaned_data["email"]
                subject = form.cleaned_data["subject"]
                recipients = ["pydevcasts@gmail.com"]

                try:
                    send_mail(
                        subject=name,  # Subject can be the name or a custom subject
                        message=f"Message: {message}\nMobile: {subject}\nFrom: {email}",
                        from_email=email,
                        recipient_list=recipients,
                    )
                except Exception as e:
                    messages.error(request, f"Error sending email: {e}")
                    return HttpResponseRedirect("contactus")

                messages.success(request, "Your message has been sent successfully!")
                return HttpResponseRedirect("")
        else:
            form = ContactusForm()

        # Optionally, you can return a response here if needed
        return HttpResponseRedirect("contactus")
