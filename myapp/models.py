from django.db import models
import uuid

# Create your models here.
class ImageModel(models.Model):
    uid = models.UUIDField( primary_key=True, editable=False, default=uuid.uuid4)
    image = models.ImageField(upload_to='image')
    watermark_text = models.CharField(max_length=100)