from django.db import models


class ContactRequests(models.Model):
    personName = models.CharField(max_length=255,null=True, blank=True, name='الأسم')
    email = models.EmailField(null=True, blank=True, name='البريد الألكترونى')
    message = models.TextField(null=True, blank=True, name='الرسالة')

    def __str__(self):
        return self.personName
