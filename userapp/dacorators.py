from django.shortcuts import redirect

def useronly(view_func):
    def wrapper(request,*args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            if group == "admin":
                return redirect('admindash')
            elif group == "user":
                return view_func(request,*args, **kwargs)
            else:
                return redirect('logoutpage')
        else:
            return redirect('logoutpage')
    return wrapper