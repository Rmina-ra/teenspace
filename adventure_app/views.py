from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Vakanсy, CustomUser, ChildProfile, Task
from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import NewUserForm, PostForm, ParentRegistrationForm, ChildRegistrationForm, EmployerRegistrationForm, VacancyForm
from django.contrib.auth.forms import AuthenticationForm
import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

categories = Category.objects.all()
vakancys = Vakanсy.objects.all()

def main_page(request):
    
    context = {
        'categories': categories,
    }
    return render(request, "./main.html", context)

def place_detail(request, pk):
    vacancys = get_object_or_404(Vakanсy, pk=pk)
    context = {
        'vacancys': vacancys
    }
    return render(request, "./place-detail.html", context)

def profile_page(request):
    return render(request, "./profile.html")

def category_by_main_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    vacancys = Vakanсy.objects.filter(category=category)
    context = {
        'category': category,
        'vacancys': vacancys,
        'categories': categories,
    }
    return render(request, "./category-by-category.html", context)

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render (request, "./sign-up.html", context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, "./login.html", context)

def logout_action(request):
    logout(request)
    return redirect('login_page')

def search_action(request):
    query = request.GET.get('q')
    vacancys = Vakanсy.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'vacancys': vacancys,
        'categories': categories
    }
    return render(request, "./results.html", context)

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    context = {
        'form': form
    }
    return redirect(request, '', context)

def delete_post(request, post_id):
    post = get_object_or_404(Vakanсy, id=post_id)
    if request.method == "POST":  
        post.delete()
        return redirect('')  
    context = {
        'post': post
    }
    return render(request, '', context)

def post_list(request):
    posts = Vakanсy.objects.all()

    context = {
        'posts': posts
    }

    return render(request, '', context)


User = get_user_model()

def register_parent(request):
    if request.method == 'POST':
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ParentRegistrationForm()
    return render(request, 'register_parent.html', {'form': form})

def register_employer(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = EmployerRegistrationForm()
    return render(request, 'register_employer.html', {'form': form})

@login_required
def register_child(request):
    if request.user.role != 'parent':
        return redirect('home')

    if request.method == 'POST':
        form = ChildRegistrationForm(request.POST)
        if form.is_valid():
            child_profile = form.save(commit=False)
            child_profile.parent = request.user
            child_profile.user = User.objects.create(username=f"child_of_{request.user.username}", role='child')
            child_profile.user.set_password('password')  # Задайте временный пароль
            child_profile.user.save()
            child_profile.save()
            return redirect('home')
    else:
        form = ChildRegistrationForm()
    return render(request, 'register_child.html', {'form': form})

def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    # Проверка, является ли пользователь владельцем задачи
    if task.owner != request.user:
        return HttpResponseForbidden("У вас нет прав для завершения этой задачи.")

    # Завершаем задачу
    task.status = 'completed'
    task.save()

    return redirect('task_detail', task_id=task.id)

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    # Возвращаем страницу с деталями задачи
    return render(request, 'task_detail.html', {'task': task})
