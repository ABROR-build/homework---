from django.shortcuts import render
from django.http import HttpResponse


def recent_posts(request):
    return HttpResponse('<h1>Recent Posts</h1>')