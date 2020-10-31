from django.shortcuts import render,get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Video
import os
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def upload(request):
    if request.method == "POST":
        videofile = request.FILES['videofile']
        thumbnail = request.FILES['thumbnail']
        video = Video(title=request.POST['title'], description=request.POST['description'], thumbnail=thumbnail, url = videofile, creator=request.user)
        video.save()
        
        return render(request, 'video/upload.html')
    
    return render(request, 'video/upload.html', {})


def view(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'video/video.html', {'video' : video})