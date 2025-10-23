from django.shortcuts import render
from .models import Conference, Conference
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

def list_Conferences(request):
    conf_list = Conference.objects.all()
    return render(request, "conference/liste.html", {"liste": conf_list})

class ConferenceList(ListView):
    model = Conference
    context_object_name = "liste"
    template_name = "conference/liste.html"

class Conferencedetail(DetailView):
    model = Conference
    context_object_name = "Conference"
    template_name = "conference/detail.html"

class ConferenceCreate(CreateView):
    model = Conference
    template_name = "conference/from.html"
    fields = "__all__"
    success_url = reverse_lazy("list_conferences")