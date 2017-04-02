from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList
from blog.models import Post
# Create your views here.

# -- List View
class PostLV(ListView) :
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

# -- Detail View
class PostDV(DetailView) :
    model = Post

# -- Archive View
class PostAV(ArchiveIndexView) :
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView) :
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView) :
    model = Post
    month_format = '%m'
    date_field = 'modify_date'

class PostDAV(DayArchiveView) :
    model = Post
    month_format = '%m'
    date_field = 'modify_date'

class PostTAV(TodayArchiveView) :
    model = Post
    month_format = '%m'
    date_field = 'modify_date'

class TagTV(TemplateView) :
    template_name = 'tagging/tagging_cloud.html'

class PostLV(ListView) :
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostTOL(TaggedObjectList) :
    model = Post
    template_name = 'tagging/tagging_post_list.html'

