from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import PostsForm

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def get_success_url(self):
        if not self.success_url:
            raise ImproperlyConfigured('No URL to redirect to')
        return str(self.success_url)    

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)



def newsline(request):
    posts = Post.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'posts' : posts,
        'rubrics' : rubrics
    }
    return render(request, 'newsline.html', context)

def rubric_list(request, rubric_id):
    posts =  Post.objects.filter(rubric=rubric_id)
    current_rubric = Rubric.objects.get(id=rubric_id)
    rubrics = Rubric.objects.all()
    context = {
        'rubrics':rubrics,
        'posts':posts,
        'current_rubric':current_rubric,

    }
    return render(request, 'rubric_list.html', context) 

def detail(request, pk):
    posts = Post.objects.get(id=pk)
    context = {
        'posts':posts
    }
    return render(request, 'detail.html', context)

def create(request):
    form = PostsForm()
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request, 'create.html', context)

def edit(request, pk):
    detail = Post.objects.get(id=pk)
    form = PostsForm(instance=detail)
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request, 'edit.html', context)

def deletes(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/')