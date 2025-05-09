from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    def __str__(self):
        return self.name
