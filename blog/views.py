from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import BlogForm, CommentForm
from .models import Blog, Comment
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs':blogs})

def blogform(request, blog_id=None):
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog_id)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.title = form.cleaned_data["title"]
            blog.body = form.cleaned_data["body"]
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('blog:detail', blog.id)
    else:
        form = BlogForm(instance=blog_id)
        return render(request, 'blog/new.html', {'form':form})

def new(request):
    return blogform(request)

def edit(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return blogform(request, blog)

def remove(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('blog:home')

def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect("blog:detail", blog_id)
    else:
        form = CommentForm()
        return render(request, "blog/detail.html", {"blog":blog, "form": form})

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect("blog:detail", comment.blog.id)


def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    blog = comment.blog
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect("blog:detail", blog.id)
    else:
        form = CommentForm(instance=comment)
        return render(request, "blog/new.html", {"form": form})

