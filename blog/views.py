from datetime import datetime
from blog.models import BlogPost,BlogPostForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


# Create your views here.

def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.timestamp=datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')

def archive(request):
    #post = BlogPost(title='danzhaoxun',body='I LOVE YOU',
    #                timestamp=datetime.now())
    #posts = BlogPost.objects.all().order_by('-timestamp')[:10]
    posts = BlogPost.objects.all()[:10]

    return render_to_response('archive.html',{'posts':posts,'form':BlogPostForm()},RequestContext(request))