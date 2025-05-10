
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField(blank=True, null=True)
    checked_out = models.BooleanField(default=False)

    def checkout(self):
        self.checked_out = True
        self.save()
        return True
    
    def return_book(self):
        self.checked_out = False
        print('CHECKED IN!')
        self.save()
        return True

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return self.name
