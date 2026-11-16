from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def mon_alarme_vue(request):
    # Votre logique de vérification de température ici...
    
    # Déclenchement de l'envoi de l'e-mail
    send_mail(
        subject="Alerte Temperature",
        message="Temperature superieure a 25 C",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["destinataire@gmail.com"],
        fail_silently=False
    )
    
    return HttpResponse("Alerte e-mail envoyée avec succès !")