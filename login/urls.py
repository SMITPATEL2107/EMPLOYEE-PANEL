from django.urls import path,include
from . import views

urlpatterns = [
  
   path("",views.Register,name="register"),
   path("adduser",views.AddUser,name="adduser"),
   path("loginpage",views.Loginpage,name="loginpage"),
   path("loginuser",views.Loginuser,name="loginuser"),
   path("showdata",views.ShowData,name="showdata"),
   path("getbyid/<int:pk>",views.GetById,name="getbyid"),
   path("getbyid1/<int:pk>",views.GetById1,name="getbyid1"),
   path("getbyid2/<int:pk>",views.GetById2,name="getbyid2"),
   path("update/<int:pk>",views.Update,name="update"),
   path("updateadmin/<int:pk>",views.UpdateAdmin,name="updateadmin"),
   path("deleteuser/<int:pk>",views.Delete,name="deleteuser"),
   
]