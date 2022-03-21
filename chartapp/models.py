from django.db import models

# Create your models here.

class Product(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    num_of_products = models.IntegerField()
    
    def __str__(self):
        return f'{self.category} - {self.num_of_products}'
    
class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    AccountID = models.CharField(max_length=50,unique=True)
    Area = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10)
    MultipleLines = models.CharField(max_length=10)
    InternetService = models.CharField(max_length=20)
    PhoneService = models.CharField(max_length=10)
    StreamingTV = models.CharField(max_length=10)
    StreamingMovies = models.CharField(max_length=10)
    TechSupport = models.CharField(max_length=10)
    FaultPowerOutagePerMonth = models.IntegerField()
    FaultCableCutPerMonth = models.IntegerField()
    Contract = models.CharField(max_length=20)
    PaperlessBilling = models.CharField(max_length=10)
    PaymentMethod = models.CharField(max_length=20)
    MonthlyCharges = models.FloatField()
    TotalCharges = models.FloatField()
    Churn = models.CharField(max_length=10)
