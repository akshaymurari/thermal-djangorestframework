from django.contrib import admin
from .models import User
# Register your models here.
def send(request):
    send_mail("meee",request.GET["inn"],"akshaymurari184@gmail.com",["akshaymurari184@gmail.com"],fail_silently=False)
    return JsonResponse({"val":True}) 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','temp','img','datetime']