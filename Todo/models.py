from django.db import models
class Todo(models.Model):
    author=models.ForeignKey("auth.user",on_delete=models.CASCADE)
    title=models.CharField(max_length=200,verbose_name="Yapılacaklar")
    completed = models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
def __str__(self):
    return self.title

# Create your models here.

