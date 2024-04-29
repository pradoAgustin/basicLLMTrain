from django.db import models

# Create your models here.
class BlogPost(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    blogger_name = models.CharField(max_length=100, default="")
    blogger_ssn = models.CharField(max_length=100, default="")
    blogger_email = models.EmailField(default="")
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

