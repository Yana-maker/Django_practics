from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from store.forms import StudentForm, SubjectForm
from store.models import Student, Contacts, Subject
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class StudentListView(ListView):
    model = Student



class StudentDetailView(DetailView):
    model = Student


class ContactsCreateView(CreateView):
    model = Contacts
    fields = ('name', 'email', 'massage',)
    success_url = reverse_lazy('store:list')

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('store:list')



class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('store:list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST)
        else:
            context_data['formset'] = SubjectFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('store:list')


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)

    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True
    student_item.save()
    return redirect(reverse('store:list'))



