from django.shortcuts import render
from .models import Post, Contact, Comment, Category
import requests
from django.http import HttpResponse


def home_view(request):
    posts = Post.objects.all()
    p = {
        'posts': posts
    }
    return render(request, "index.html", p)


def about_view(request):
    return render(request, "about.html")


def contact_view(request):
    if request.method == "POST":
        data = request.POST
        obj = Contact.objects.create(name=data['name'], email=data['email'], subject=data['subject'],
                                     message=data['message'])

        obj.save()
        url = f"https://api.telegram.org/bot6560757196:AAGILjAVAkw5C4-2eNV-Wm7abs4KbCbd090/sendMessage?chat_id=748076346&text=you have a notification from readit website:{data['message']}"
        result = requests.get(url)

    return render(request, "contact.html")


def blog_view(request):
    data = request.GET
    cat_id = data.get("cat_id")
    cat_obj = Category.objects.get(id=cat_id)
    posts = Post.objects.filter(category=cat_obj)

    d = {
        'posts': posts
    }
    return render(request=request, template_name="blog.html", context=d)


def blog_single_view(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)
    categories = Category.objects.all()

    d = {
        'post': post,
        'comments': comments,
        "categories": categories
    }

    if request.method == "POST":
        data = request.POST
        obj = Comment.objects.create(name=data['name'], email=data['email'], website=data['website'],
                                     message=data['message'], post=post)
        obj.save()

        return render(request=request, template_name="blog-single.html", context=d)

    return render(request=request, template_name="blog-single.html", context=d)
