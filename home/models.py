from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self) -> str:
        return self.name

class Gallery(models.Model):
    title=models.CharField(max_length=150)
    detail=models.TextField()
    
    def __str__(self) -> str:
        return self.title

class SubPlan(models.Model):
    title=models.CharField(max_length=150)
    price=models.IntegerField()
    highlight_status=models.BooleanField(default=False, null=True)

    def __str__(self) -> str:
        return self.title

class SubPlanFeature(models.Model):
    subplan=models.ForeignKey(SubPlan, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title



