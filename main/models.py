from django.db import models

# Create your models here.
class Work(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    work_image = models.ImageField(upload_to='uploads/')
    work_number = models.IntegerField()

    def __str__(self):
        return self.name
    
class Review(models.Model):
    review = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)

    def __str__(self):
        return self.work.name
    
class Message(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email