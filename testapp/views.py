from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView,DetailView,DeleteView
from .models import Employee
from django.urls import reverse_lazy


class EmpList(ListView):
    model = Employee
    template_name = 'list.html'

class Create(CreateView):
    model = Employee
    template_name = 'create.html'
    fields = ("__all__")

class detail(DetailView):
    model = Employee
    template_name = 'detail.html'

class update(UpdateView):
    model = Employee
    template_name = 'update.html'
    fields = '__all__'
class delete(DeleteView):
    model = Employee
    template_name = 'delete.html'
    success_url = reverse_lazy('list')


