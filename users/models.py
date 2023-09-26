from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        # Run save method of parent class by using 'super()'
        super().save()
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            
