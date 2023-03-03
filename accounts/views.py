from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from accounts.dacorators import unauth_user
# Create your views here.

@method_decorator(unauth_user,name='dispatch')
class Loginview(View):
    def get(self,request):
        return render(request,'accounts/login.html')
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get("password")
        print(f'{username} and {password}')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            print(request.user)
            group =None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group =='admin':
                    print('this user is an admin')
                    return redirect('admindash')
                elif group == 'user':
                    print('this user is an user')
                    return redirect('userdash')
                else:
                    return redirect('logoutpage')
        else:
            return redirect('admindash')
            
        # return HttpResponseRedirect(reverse_lazy(''))
        
        

def logout_view(request):
    logout(request)
    return redirect('loginpage')