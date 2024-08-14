from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.forms.login_form import LoginModelForm
from app.forms.others import CommentForm, FeedbackModelForm, ProductModelForm
from app.forms.register_form import RegisterModelForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Room, Blog, Comment
from hotel_uz import settings


def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = RegisterModelForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = RegisterModelForm()
    return render(request=request,
                  template_name='app/auth/register.html',
                  context={"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = LoginModelForm(request=request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request=request,
                      user=user)
                return redirect('index')
        else:
            form = LoginModelForm()
    return render(request=request,
                  template_name='app/auth/login.html',
                  context={"form": form})


@login_required(login_url="login")
def logout_view(request):
    logout(request=request)
    return redirect('index')


def index(request):
    blogs = Blog.objects.all()
    rooms = Room.objects.all()
    return render(request=request,
                  template_name='app/index.html',
                  context={'rooms': rooms,
                           'blogs': blogs})


def rooms(request):
    rooms = Room.objects.all()
    query = request.GET.get("query")
    if query:
        rooms = Room.objects.filter(title__icontains=query
                                    )
    return render(request=request,
                  template_name='app/rooms.html',
                  context={'rooms': rooms})


def restaurant(request):
    return render(request=request,
                  template_name='app/restaurant.html')


def about(request):
    return render(request=request,
                  template_name='app/about.html')


def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(object_list=blogs,
                          per_page=3)
    page_number = request.GET.get("page")
    blogs_list = paginator.get_page(number=page_number)
    return render(request=request,
                  template_name='app/blog.html',
                  context={'blogs_list': blogs_list})


def blog_detail(request, blog_id):
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-detail', blog_id=blog_id)
    blog = Blog.objects.filter(id=blog_id).first()
    blogs = Blog.objects.order_by("-created_at")[:3]
    comments = Comment.objects.all()[:3]
    comment_one = Comment.objects.all()[:1]

    return render(request=request,
                  template_name='app/blog-single.html',
                  context={'blog': blog,
                           "blogs": blogs,
                           "comments": comments,
                           "comment_one": comment_one})


def contact(request):
    if request.method == "POST":
        form = FeedbackModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ProductModelForm()
    return render(request=request,
                  template_name='app/contact.html',
                  context={"form": form})


def room_detail(request, room_id):
    room = Room.objects.filter(id=room_id).first()
    rooms = Room.objects.order_by('-price')[:2]
    blogs = Blog.objects.order_by("-created_at")[:3]
    return render(request=request,
                  template_name='app/rooms-single.html',
                  context={'room': room,
                           "rooms": rooms,
                           "blogs": blogs})


# @login_required(login_url='login')

@login_required(login_url='login')
def new_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        Comment.objects.create(
            user=request.user,
            blog=blog,
            text=request.POST['text']
        )
        messages.info(request, 'Successfully Sended!')
        return redirect('blog-detail', blog_id)
    return HttpResponse("add comment")
