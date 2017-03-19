from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
# Create your views here.

# --- List View
class BookmarkLV(ListView):
	model = Bookmark

# --- Detail View
class BookmarkDV(DetailView):
	model = Bookmark