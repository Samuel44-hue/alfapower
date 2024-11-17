from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('UploadProduct/',views.Upload_Product, name="Upload_Product"),
    path('Product/',views.Product, name='Product'),
    path('AdminMenu/',views.AdminMenu, name="AdminMenu"),
    path('UpdateProduct/<int:Product_id>/',views.UpdateProduct,name='UpdateProduct'),
    path('DeleteProduct/<int:Product_id>/',views.DeleteProduct, name="DeleteProduct"),
    path('DetailProduct/<int:Product_id>/',views.DetailProduct,name="DetailProduct"),
    path('UploadProject/',views.Upload_Project, name='UploadProject'),
    path('UpdateProject/<int:Project_id>/',views.UpdateProject, name='UpdateProject'),
    path('DeleteProject/<int:Project_id>/',views.DeleteProject, name='DeleteProject'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('detailsgiven/', views.contact_view, name='contact_view'),

]