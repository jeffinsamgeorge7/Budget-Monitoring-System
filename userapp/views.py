import datetime
from itertools import groupby
from django.db.models import F
from django.db.models.aggregates import Sum
from django.http.response import HttpResponse, HttpResponseRedirect
from administrator.models import Budget, Department
from django.urls.base import reverse, reverse_lazy
from userapp.forms import ExpenseForm, ProfileUpdate
from userapp.models import Expense
from django.shortcuts import redirect, render
from django.views.generic import View, CreateView
from django.contrib.auth.models import User
from typing import Final
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from userapp.dacorators import useronly
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
# Create your views here.

dacorator =[login_required,useronly]
@method_decorator(dacorator,name='dispatch')
class ExpenseCreate(CreateView):
    model = Expense
    form_class = ExpenseForm
    success_url = reverse_lazy('expenselist')
    template_name = "user/form.html"
    
    def get_context_data(self, *args,**kwargs) :
        context =super().get_context_data(*args,**kwargs)
        context['head'] = "expense create"
        return context

    def form_valid(self, form): 
        form.instance.user = self.request.user
        # department = form.cleaned_data['department']
        department = self.request.user.head.department
        print(department)
        amount = form.cleaned_data['amount']
        x=Department.objects.filter(name__iexact=department.name)
        form.instance.department =department
        x.update(balance=F('balance')-amount)
        return super().form_valid(form)
    
    def form_invalid(self, form) :
        print(form.errors)
        return super().form_invalid(form)

@method_decorator(dacorator,name='dispatch')
class ExpenseView(View):
    def get(self, request, *args, **kwargs):
        try:
            data = Expense.objects.filter(
                department=request.user.head.department)
        except:
            data = ''
        context = {
            'data': data,
            
        }
        return render(request, 'user/expense.html', context)

@login_required
@useronly
def ExpenseUpdate(request, pk):
    obj_data = Expense.objects.get(id=pk)
    a: Final = obj_data.amount
    print(f"{a} is instance")
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=obj_data)
        if form.is_valid():
            obj = form.save(commit=False)
            x = obj.amount
            print(f"{x} is the input")
            sum = a-x
            sumx = -sum
            Department.objects.filter(name__iexact=obj.department).update(
                balance=F('balance')-sumx)
            obj.save()
            return redirect(reverse('expenselist'))
        
        # if x < a:
        #     print("a is greater than x")
        #     sum = x-a
        #     x=Department.objects.get(name__iexact=obj.department)
        #     x.update(balance=F('balance')+sum)
        #     print(x)

        # elif x > a:
        #     sum = x-a
        #     print(sum)
        #     print("x is greater than  a")
        # else:
        #     print("those are equal")
    context = {
        'form': ExpenseForm(instance=obj_data),
        'head':"Expense update"
    }
    print(request.user)
    return render(request, 'user/form.html', context)

@method_decorator(dacorator,name='dispatch')
class UserDashboard(View):
    def get(self, *args, **kwargs):
        
        slug =self.request.user.head.department
        dep= Department.objects.get(id=slug.id)
        dep_sum = Expense.objects.filter(department=slug).aggregate(Sum('amount'))
        bud_sum = Budget.objects.filter(department=slug).aggregate(Sum('amount'))
        this_month = datetime.datetime.now().month
        dep_month_sum = Expense.objects.filter(department=slug , date__month=this_month).aggregate(Sum('amount'))
        print(dep_month_sum)
        
        ind = Expense.objects.filter(department=slug).only('date', 'amount').order_by('date')
        x =[]
        y=[]
        month_totals = {
             y.append(k):x.append(sum(x.amount for x in g) )
            for k, g in groupby(ind, key=lambda i: i.date.strftime('%B'))
        }
        context = dict()
        context['label']=x
        context['datas'] =y
        context['exp_sum'] = dep_sum['amount__sum']
        context['bud_sum'] = bud_sum['amount__sum']
        context['department'] =dep
        context['dep_month_sum'] = dep_month_sum['amount__sum']
        context['budget'] = Budget.objects.filter(department=slug)
        context['expense'] = Expense.objects.filter(department=slug)
        return render(self.request,'user/dashboard.html',context)


@method_decorator(dacorator,name='dispatch')
class BudgetView(View):
    def get(self,request):
        try:
         x=Budget.objects.filter(department=request.user.head.department)
        except:
            x = []
        context={
            'budget':x
        }
        
        return render(request,'user/budget.html',context)
    

class ProfileView(View):
    def get(self,request):
        form = ProfileUpdate(instance=request.user)
        context = {
            'form':form,
            'head':"profile update"
        }
        return render(request,'user/form.html',context)
    
    def post(self,request, *args, **kwargs):
        form = ProfileUpdate(request.POST or None,instance=request.user)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your user credentials was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('userprofile'))
        else:
        
            messages.error(request, form.errors)
            return HttpResponseRedirect(reverse_lazy('userprofile'))
            
            
        
    
def  home(request):
    return redirect('loginpage') 