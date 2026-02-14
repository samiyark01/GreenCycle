from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    eco_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username  
class PickupRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    pickup_address = models.TextField()
    description = models.TextField(blank = True)
    STATUS_CHOICES = [
        ('PENDING','pending'),
        ('COLLECTED','collected'),
        ('RECYCLED','Recycled'),
    ]
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    request_at = models.DateTimeField(auto_now_add=True)
    def save(self,*args,**kwargs):
        if self.pk:
            old_request = PickupRequest.objects.get(pk=self.pk)
            if old_request.status != 'RECYCLED' and self.status =='RECYCLED':
                profile = self.user.userprofile
                profile.eco_points += self.quantity*10
                profile.save() 
                self.user.userprofile.save()
        super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.user.username}-{self.item_name}"
from django.db.models.signals import post_save     
from django.dispatch import receiver            
@receiver(post_save,sender = User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)