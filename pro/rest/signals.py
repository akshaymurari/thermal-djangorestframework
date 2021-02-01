from .models import User
from django.db.models.signals import post_save,post_delete
from django.core.mail import send_mail
from django.dispatch import receiver
from .serializer import UserSerializer
import json
@receiver(post_save,sender=User)
def send(sender,instance,created,**kwargs):
    serializer = UserSerializer(instance)
    print(json.dumps(serializer.data))
    # print(serializer.data.get("temp"))
    if created and float(serializer.data.get("temp"))>=99:
        send_mail("from thermal section",'http://127.0.0.1:8000'+serializer.data.get("img"),"akshaymurari184@gmail.com",["akshaymurari184@gmail.com"],fail_silently=False)
@receiver(post_delete,sender=User)
def delete(sender,instance,**kwargs):
    created = False
    print("from delete")
    if instance is not None:
        serializer = UserSerializer(instance)
        print(serializer.data)
        if created:
            send_mail("from thermal section","case reported","akshaymurari184@gmail.com",["akshaymurari184@gmail.com"],fail_silently=False)
            print("hii")
    else:
        print("instance is none")