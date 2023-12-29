from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Photo
# Create your views here.

class PhotoListView(ListView):
	model = Photo
	template_name = 'photoapp/list.html'
	context_object_name = 'photos'

class PhotoTagListView(PhotoListView):
	template_name = 'photoapp/taglist.html'
	
	def get_tag(self):
		return self.kwargs.get('tag')
	
	def get_queryset(self):
		return self.model.objects.filter(tags__slug=self.get_tag())
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["tag"] = self.get_tag()
		return context
	