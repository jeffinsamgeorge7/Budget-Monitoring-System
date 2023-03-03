from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.expressions import OrderBy
from django.shortcuts import reverse
from django.core.validators import MinValueValidator
from django.template.defaultfilters import slugify
from django.db.models import Sum


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    balance = models.FloatField(blank=True, null=True, validators=[MinValueValidator(
        0.00, message="you dont have enough budget to raise fund")], default=0)
    timestamp = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    @property
    def budgetsum(self):
        
        obj =self.budget_set.all().aggregate(total=Sum('amount'))
           
        print(obj)
        return obj['total']
    
    @property
    def expsum(self):
        obj =self.expense_set.all().aggregate(total=Sum('amount'))
           
        print(obj)
        return obj['total']
        
    
    
    def  save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        return super(Department,self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("depdetail", kwargs={"slug": self.slug})
    
    
    def get_update_url(self):
        return reverse("depupdate", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Head(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.OneToOneField(Department, models.CASCADE,blank=True,null=True)
    join_date = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)

    def get_update_url(self):
        return reverse('headupdate',kwargs={'pk':self.pk})

    class Meta:
        unique_together = ('user','department')

    def __str__(self):
        return str(self.user)


class Budget(models.Model):
    name = models.CharField(max_length=100,unique=True)
    desc = models.TextField()
    amount = models.FloatField(validators=[MinValueValidator(0, message="you should enter a valid amount")])
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-date']

    @property
    def balance(self):
        obj = self.department.objects.get(id=self.department)
        return obj

    @property
    def fdate(self):
        return self.date.strftime('%d-%m-%Y')
    
    def __str__(self):
        return self.name