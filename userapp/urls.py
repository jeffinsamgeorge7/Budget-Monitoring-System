from userapp.views import BudgetView, ExpenseCreate, ExpenseUpdate, ExpenseView, ProfileView, UserDashboard,home
from django.urls import  path

urlpatterns = [
    path('expense/create/',ExpenseCreate.as_view(),name="expensecreate"),
    path('expense/',ExpenseView.as_view(),name="expenselist"),
    path('expense/<int:pk>/update/',ExpenseUpdate,name="expenseupdate") ,
    path('dashboard/',UserDashboard.as_view(),name="userdash")  ,
    path('budget/',BudgetView.as_view(),name="budget")  ,
    path('profile/',ProfileView.as_view(),name="userprofile")  ,
    path('',home,name="home")  ,
    
]
