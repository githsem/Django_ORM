from django.db import models
from django.utils import timezone

# Create your models here.

class BookContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class BookOrders(BookContent):
    class Meta:
        proxy = True
        ordering = ['created']  

    def created_on(self):
        return timezone.now() - self.created      

class Books(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class ISBN(Books):
    books_ptr = models.OneToOneField(
        Books, on_delete=models.CASCADE, 
        parent_link=True, primary_key=True,
    )
    ISBN = models.TextField()    

class BaseItem(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['title']

class ItemA(BaseItem):
    content = models.TextField()        

    class Meta(BaseItem.Meta):
        ordering = ['-created']

class ItemB(BaseItem):
    file = models.FileField(upload_to='files')   

class ItemC(BaseItem):
    file = models.FileField(upload_to='images') 

class ItemD(BaseItem):
    slug = models.SlugField(max_length=255, unique=True)