from django.shortcuts import render
from django.http import HttpResponse


def post_list(request):
    # return HttpResponse('Hello world')
    return render(request, 'blog/post_list.html', {})
