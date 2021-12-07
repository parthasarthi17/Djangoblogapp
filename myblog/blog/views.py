from django.shortcuts import render, redirect
from .models import Author, Article, comments, tempUser
from .forms import ArticlForm, commentForm, tempform, RegisterForm
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse


# Create your views here.

def index(request):
    dataset = Author.objects.all()
    context = {
        'dataset' : dataset,
    }

    return render(request,"index.html", context)

def authorview(request, id):
    data = Author.objects.get(id=id)
    form = ArticlForm()
    context = {
    'data':data,
    'forms':form,
    }

    return render(request,"authorview.html", context)

def ArticleViews(request, id):
    data = Article.objects.get(id=id)

    context = {
    'data' : data,
    }

    return render(request, "ArticleViews.html", context)


def add(request):
    if request.method == "POST":
        form = ArticlForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.author = Author.objects.get(user__username=request.user.username)
            form.save()
            id = request.user.id
            return redirect('blog:authorview', id)
    form = ArticlForm()
    context = {
    'forms':form,
    }

    return render(request, 'add.html', context)


def remove(request, id):
    item = Article.objects.get(id=id)
    item.delete()
    id = request.POST.get('tag_id')
    print(id)

    return redirect('blog:authorview' , id)

def commentsView(request, id):
    if request.method == "POST":
        form = commentForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.post = Article.objects.get(id=id)
            obj.writer = request.user
            form.save()
            return redirect('blog:articles' , id)
    form = commentForm()
    context = {
    'forms':form,
    }

    return render(request, 'comments.html', context)


def registerview(request):
    if request.method == 'POST':
        form = tempform(request.POST)
        print(request.POST)

        if form.is_valid():
            obj=form.save(commit=False)
            obj.unique=get_random_string(6)
            obj.save()
            return redirect('blog:peeps',obj.tempname)
    form = tempform()
    context = {
    'forms':form,
    }


    return render(request,"registeruser.html", context)

def personview(request, name):

    data = tempUser.objects.get(tempname=name)
    context = {
    'data' : data,
    }

    print(data.tempname)
    print(data.unique)


    return render(request, 'persons.html', context)


def checkview(request, name):
    item = tempUser.objects.get(tempname=name)
    qwerty = request.POST.get('Person_name')

    print(item.unique)
    print(item.emailid)
    print(qwerty)


    if f"{item.unique}" == qwerty:
        UUU =request.POST.get('Username')
        EEE =request.POST.get('email')
        PPPP =request.POST.get('Pass_1')

        newUser = User.objects.create(username=UUU, email=EEE, password=PPPP)
        item.delete()
        return HttpResponse('New User Created!!')

    else:
        return HttpResponse('incorrect OTP')
