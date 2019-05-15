from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import BlogForm
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs':blogs})

def blogform(request, blog=None):
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'blog/new.html', {'form':form})

def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blogform(request, blog)

def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')
