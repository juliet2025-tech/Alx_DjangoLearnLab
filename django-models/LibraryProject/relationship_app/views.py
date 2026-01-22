from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

'relationship_app/librarian_view.html'
'relationship_app/member_view.html'


# Registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('login')
    else:
        form = AuthenticationForm()

    return render(request, 'relationship_app/login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# ===== ROLE CHECK =====
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# ===== ADMIN VIEW =====
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        Book.objects.create(
            title=title,
            author=author,
            published_date=published_date
        )
        return redirect('list_books')
    return render(request, 'relationship_app/add_book.html')

"relationship_app.can_change_book"
"relationship_app.can_delete_book"

"relationship_app/list_books.html"
"Book.objects.all()"
