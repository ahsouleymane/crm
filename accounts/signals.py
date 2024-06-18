from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer
from django.contrib.auth.models import Group

""" Les signaux Django sont une sorte de canal de communication qui permet aux
applications découplées d'être averties lorsque certaines actions se produisent ailleurs
dans l'application. Voici comment ils fonctionnent :

Senders : parties de votre application qui effectuent une action, puis envoient un
signal. 

Receivers : fonctions ou méthodes qui écoutent un signal spécifique à envoyer, 
puis agissent dès la réception de ce signal.
Ils sont utiles pour créer des rappels lorsque des événements tels que l'enregistrement 
ou la suppression d'une instance se produisent. Vous souhaitez savoir comment les mettre 
en œuvre ? """

#@receiver(post_save, sender=User)  
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username,
        )
        
        print('Profil créé avec succès !')
        
post_save.connect(customer_profile, sender=User)

#@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profil mis à jour avec succès !')
        
#post_save.connect(update_profile, sender=User)
