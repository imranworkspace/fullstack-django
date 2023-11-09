from django.db import models

# Create your models here.
class StudentModel(models.Model):
    mystream = [
        ('bca','BCA'),
        ('mca','MCA')]
    s_id = models.BigAutoField(primary_key=True)
    f_name = models.CharField(max_length = 150)
    l_name = models.CharField(max_length = 150)
    stream = models.CharField(max_length = 150,choices=mystream)

    def __str__(self) -> str:
        return self.f_name
    