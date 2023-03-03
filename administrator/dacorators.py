from django.shortcuts import redirect

def adminonly(view_func):
    def wrapper(request,*args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            if group == "admin":
                return view_func(request,*args, **kwargs)
            elif group == "user":
                return redirect('userdash')
            else:
                return redirect('logoutpage')
        else:
            return redirect('logoutpage')
    return wrapper
            