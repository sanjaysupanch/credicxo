from django.db import models


class banks(models.Model):
   name = models.CharField(max_length=49)
   id=models.BigIntegerField(primary_key=True)

   class Meta:
        db_table = 'banks'
   

class branches(models.Model):
   ifsc=models.CharField(max_length=11, null=False, primary_key=True)
   bank=models.ForeignKey(banks, on_delete=models.CASCADE)
   branch= models.CharField(max_length=74)
   address=models.CharField(max_length=195)
   city=models.CharField(max_length=50)
   district=models.CharField(max_length=50)
   state=models.CharField(max_length=26)

   class Meta:
        db_table = 'branches'

class bank_branches(models.Model):
   ifsc=models.CharField(max_length=11, null=False, primary_key=True)
   bank_id=models.BigIntegerField()
   branch= models.CharField(max_length=74)
   address=models.CharField(max_length=195)
   city=models.CharField(max_length=50)
   district=models.CharField(max_length=50)
   state=models.CharField(max_length=26)
   bank_name=models.CharField(max_length=49)

   class Meta:
        db_table = 'bank_branches'
