from django.shortcuts import render
from post.models import Post
from categories.models import Catagory
def home(request,category_slug = None):
    posts = Post.objects.all()
    if category_slug:
        category = Catagory.objects.get(slug=category_slug)
        posts = Post.objects.filter(category=category)
    categories = Catagory.objects.all()
    return render(request, 'home.html',{'post' : posts,'categories' : categories})