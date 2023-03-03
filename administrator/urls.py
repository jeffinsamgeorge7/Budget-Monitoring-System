from administrator.models import Department
from administrator.views import AdminDashView, BudgetCreate, BudgetList, DepDelete, DepartmentCreate, DepartmentDetailView, DepartmentList, DepartmentUpdate, HeadDelete, HeadList, HeadUpdate, HeadView, UserList, userDelete
from django.urls import path

urlpatterns = [
    path('department/create/',DepartmentCreate.as_view(),name="depcrete"),
    path('department/',DepartmentList.as_view(),name="dep"),
    path('department/<int:pk>/update/',DepartmentUpdate.as_view(),name="depupdate"),
    path('department/<slug>/report/',DepartmentDetailView.as_view(),name="depdetail"),
    path('department/<int:pk>/delete/',DepDelete,name="depdelete"),
    path('budget/create/',BudgetCreate.as_view(),name="budcrete"),
    path('budget/',BudgetList.as_view(),name="budlist"),
    path('head/',HeadList.as_view(),name="headlist"),
    path('head/create/',HeadView.as_view(),name="headcreate"),
    path('head/<int:pk>/update',HeadUpdate.as_view(),name="headupdate"),
    path('head/<int:pk>/delete',HeadDelete,name="headdelete"),
    path('users/',UserList.as_view(),name="userlist"),
    path('user/<int:pk>/delete/',userDelete,name="userdelete"),
    path('',AdminDashView.as_view(),name="admindash")
]