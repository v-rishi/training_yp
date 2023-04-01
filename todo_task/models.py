from django.db import models

# Create your models here.
import uuid


from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)


class Task(models.Model):
    UNDEFINED = 'UD'
    TASK_STATUS_CHOICES = [
        ("In-Progress", "IP"),
        ("Completed", "CP")
    ]
    title = models.CharField("Title", max_length=255)
    description = models.CharField("Description", max_length=255)
    status = models.CharField(
        max_length=15,
        choices=TASK_STATUS_CHOICES,
        default=UNDEFINED,
    )


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name="task", on_delete=models.PROTECT)
    comment = models.CharField("Comments", max_length=255)
   
    class Meta:
        pass