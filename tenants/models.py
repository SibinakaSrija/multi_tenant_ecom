from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    domain = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.domain})"
