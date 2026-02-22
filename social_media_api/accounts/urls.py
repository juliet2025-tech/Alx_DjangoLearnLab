from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
]

from django.urls import path
from .views import follow_user, unfollow_user

urlpatterns = [
    path('follow/<int:user_id>/', follow_user),
    path('unfollow/<int:user_id>/', unfollow_user),
]