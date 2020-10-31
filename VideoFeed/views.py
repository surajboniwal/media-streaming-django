from django.shortcuts import render,get_list_or_404
from video.models import Video
from django.http import Http404

def index(request):
    videolist = get_list_or_404(Video.objects.order_by('upload_date'))
    context = {
        'videolist' : videolist
    }
    return render(request, 'videofeed/index.html', context)


def library(request):
    return render(request, 'videofeed/library.html')