from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def home(request):
    page = request.GET.get('page', '1')
    blog_list = Blog.objects.order_by('-pub_date')
    paginator = Paginator(blog_list, 10)
    page_obj = paginator.get_page(page)
    context = {'blog_list': page_obj}
    return render(request, 'blog/home.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {'blog':blog}
    return render(request, 'blog/blog_detail.html', context)

@login_required(login_url='common:login')
def comment_create(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.pub_date = timezone.now()
            comment.blog = blog
            comment.save()
            return redirect('blog:detail', blog_id=blog.id)
    else:
        form = CommentForm()
    context = {'blog': blog, 'form': form}
    return render(request, 'blog/blog_detail.html', context)

@login_required(login_url='common:login')
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author =request.user
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('blog:home')
    else:
        form = BlogForm()
    context = {'form':form}
    return render(request, 'blog/blog_form.html', context)