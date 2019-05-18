from django.urls import path
from . import views

urlpatterns = [
    path('',views.book_list,name ='book_list'),
    path('create/',views.book_create, name='create'),
    path('edit/<int:book_id>/',views.book_update,name = 'edit'),
    path('delete/<int:book_id>/',views.book_delete, name ='delete'),
    path('view/<int:book_id>/',views.view_book,name = 'view'),
]
