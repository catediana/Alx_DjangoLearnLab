from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Creating models.

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    # Establishes a many-to-one relationship: many books to one author.
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE, 
        related_name='books'
    )
     
    def __str__(self):
        return self.author
    
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(
        Book,
        related_name = 'Library'
    )
    
    def __str__(self):
        return self.name ,self.books

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library, 
        on_delete=models.CASCADE,  
        related_name='librarian'
    )
    
    def __str__(self):
        return self.name , self.library
    


# Define the role choices.
ROLE_CHOICES =[
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

#  UserProfile when a new User is created.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Default role is set to 'Member'; adjust as needed.
        UserProfile.objects.create(user=instance, role='Member')

# Ensure the profile is saved when the user is saved.
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
