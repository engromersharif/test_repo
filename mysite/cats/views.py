from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed

# Create your views here.
class CatList(LoginRequiredMixin, ListView):
    model = Cat
    template_name = 'cats/cat_list.html' # <app_name>/blog_list.html
    context_object_name = 'object_list' # Default is object_list if not specified

class CatDetail(LoginRequiredMixin, DetailView):
    model = Cat
    template_name = 'cats/cat_detail.html' # <app_name>/blog_list.html
    context_object_name = 'object_list' # Default is object_list if not specified

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedList(LoginRequiredMixin, ListView):
    model = Breed
    template_name = 'cats/breed_list.html' # <app_name>/blog_list.html
    context_object_name = 'object_list' # Default is object_list if not specified

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breedlist')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breedlist')

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breedlist')

