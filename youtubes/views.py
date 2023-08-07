from django.shortcuts import render
from django.views import generic
from .models import Video , Comment 
# Create your views here.

class VideoList(generic.ListView):
    model = Video

class VideoDetail(generic.DetailView):
    model=Video

class CommentList(generic.ListView):
    model = Comment

class CommentDetail(generic.DetailView):
    model=Comment