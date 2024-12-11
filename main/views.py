from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import auth
from django.urls import reverse
from main.forms import HelpInputForm, UserInputForm, UserLoginForm, UserRegistrationForm
from main.models import Favorite, ychebniki, User
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        favorite_books = Favorite.objects.filter(user=request.user)
        data = {'favorite_books': favorite_books,}
        return render(request, 'main/home.html', data)
    else:
        return render(request, 'main/home.html')

def rzadach(request):
    try:
        text_obj=User.objects.get(id=request.user.id)
        text1 = text_obj.text
    except:
        text1=''

    if request.user.is_authenticated:
        favorite_books = Favorite.objects.filter(user=request.user)
        data = {'text1': text1,
                'favorite_books': favorite_books,}
        return render(request, 'main/rzadach.html', data)
    else:
        data = {'text1': text1,}
        return render(request, 'main/rzadach.html',data)

def reshebniki(request):

    if request.user.is_authenticated:
        favorite_books = Favorite.objects.filter(user=request.user)
        data = {'favorite_books': favorite_books,}
        return render(request, 'main/reshebniki.html', data)
    else:
        return render(request, 'main/reshebniki.html')

def razrab(request):
    if request.user.is_authenticated:
        favorite_books = Favorite.objects.filter(user=request.user)
        data = {'favorite_books': favorite_books,}
        return render(request, 'main/razrab.html', data)
    else:
        return render(request, 'main/razrab.html')

def ychebnik(request):
    if request.user.is_authenticated:
        favorite_books = Favorite.objects.filter(user=request.user)
        sbornik = ychebniki.objects.filter(category__name='Учебник')
        data = {'sbornik': sbornik,
                'favorite_books': favorite_books,}
        return render(request, 'main/ychebniki.html', data)
    else:
        sbornik = ychebniki.objects.filter(category__name='Учебник')
        data = {'sbornik': sbornik,}
        return render(request, 'main/ychebniki.html', data)

def sbor(request):
    if request.user.is_authenticated:
        favorite_books = Favorite.objects.filter(user=request.user)
        sbornik = ychebniki.objects.filter(category__name='Сборник')
        data = {'sbornik': sbornik,
                'favorite_books': favorite_books,}
        return render(request, 'main/sbor.html', data)
    else:
        sbornik = ychebniki.objects.filter(category__name='Сборник')
        data = {'sbornik': sbornik,}
        return render(request, 'main/sbor.html', data)

def registration(request):

    formReg = UserRegistrationForm(data=request.POST)
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        formReg = UserRegistrationForm(data=request.POST)
        if formReg.is_valid():
            formReg.save()
            user = formReg.instance
            auth.login(request, user)
            return redirect(url)
        
    data = {'formReg': formReg,}
    return render(request, 'main/home.html', data)

def login(request):

    form = UserLoginForm(data=request.POST)
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            User = auth.authenticate(username=username, password=password)
            if User:
                auth.login(request, User)
                return redirect(url)
            
    data = {'form': form,}
    return render(request, 'main/home.html', data)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))

def TextSave(request):
    form = UserInputForm(request.POST, instance=request.user)
    url = request.META.get('HTTP_REFERER')
    try:
        text_obj=User.objects.get(id=request.user.id)
        text1 = text_obj.text
    except:
        text1=' '

    if request.method == 'POST':
        form = UserInputForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(url)
        
    data = {'form': form,
            'text1': text1}
    return render(request, 'main/rzadach.html', data)

def add_to_favorites(request, book_id):
    url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        book = get_object_or_404(ychebniki, id=book_id)
        Favorite.objects.get_or_create(user=request.user, book=book)
        return redirect(url)  # Замените на ваш URL
    else:
        return redirect(url)
    
def remove_from_favorites(request, book_id):
    url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        book = Favorite.objects.get(id=book_id)
        book.delete()
        return redirect(url)
    else:
        return redirect(url)
    
@login_required
def userHelp(request):

    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = HelpInputForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(url)
    else:
        form = HelpInputForm(request.POST, instance=request.user)
        
    data = {'form': form,}
    return render(request, 'main/razrab.html', data)

    
