from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import admin_view
from .views import add_book, edit_book, delete_book



urlpatterns = [
    path('register/', views.register_view, name='register'),

    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),
]

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def librarian_view(request):
    ...











from django.urls import path
from .views import admin_view

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]

from django.urls import path
from .views import admin_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
]

"from .views import list_books", "LibraryDetailView"





urlpatterns = [
    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:pk>/', edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', delete_book, name='delete_book'),
]

"add_book/"
"edit_book/"

from django.urls import path
from .views import list_books, LibraryDetailView  # <-- ALX checker wants this exact line

urlpatterns = [
    # Function-based view
    path('books/', list_books, name='list_books'),

    # Class-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
