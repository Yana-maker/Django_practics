from django.shortcuts import render
from django.urls import reverse_lazy

from store.models import Student, Contacts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class StudentListView(ListView):
    model = Student
    template_name = 'store/material_list.html'

class StudentDetailView(DetailView):
    model = Student


class ContactsCreateView(CreateView):
    model = Contacts
    fields = ('name', 'email', 'massage',)
    success_url = reverse_lazy('store:list')

class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'second_name', 'avatar',)
    success_url = reverse_lazy('store:list')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'second_name', 'avatar',)
    success_url = reverse_lazy('store:list')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('store:list')
