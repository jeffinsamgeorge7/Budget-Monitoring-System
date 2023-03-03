from django.shortcuts import redirect

def unauth_user(view_func):
    def wrapper(request,*args, **kwargs):
        if request.user.is_authenticated:
            print('authenticated')
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
                return redirect('logoutpage')
        else:
            return view_func(request,*args, **kwargs)
    return wrapper
            