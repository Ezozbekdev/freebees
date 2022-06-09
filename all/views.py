from django.shortcuts import render
from .models import (
    About, Blog, Profile,
)
from .forms import ContactForm


def Blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)

    return render(request, 'all/single-post.html', {
        'blog': blog
    })


def BlogViews(request):
    blog = Blog.objects.all()

    context = {
        'blog': blog
    }
    return render(request, 'all/blog.html', context)


def main(request):
    return render(request, 'all/index.html')


def about(request):
    ab = About.objects.all()
    context = {
        'about': ab
    }
    return render(request, 'all/about.html', context)


def profile(request):
    profile = Profile.objects.all()

    context = {
        'pro': profile
    }
    return render(request, 'all/portfolio.html', context)


def ContactViews(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }

    return render(request, 'all/contact.html', context)
