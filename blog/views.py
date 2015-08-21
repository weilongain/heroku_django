from django.shortcuts import render
from django.views import generic
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    post_list = models.Post.objects.filter(publish="True").order_by("-postime")
    paginator = Paginator(post_list, 3) # Show 3 contacts per page
    page = request.GET.get("page")
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    #以上是部落格列表

    top=models.TopPost.objects.get(id=1).post_set.all().filter(publish="True").order_by("-postime")



    text={"postlis":post,"Toplis":top}
    return render(request, 'index.html',text )


def blogPost(request,pk):
    try:
        queryset = models.Post.objects.get(id=pk)
        if queryset.publish == True:
            context = {"queryset":queryset}
            return render(request,"post.html",context)
        else:
            return render(request, 'index.html',)
    except:
        return render(request, 'index.html',)


def about(request):
    return render(request,"about.html")
