import Image
import ImageTk
import os
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from mongoengine import *
from polls.models import Post
from polls.models import Rating


def getImages():
    db = connect("mydb")
    picarray = []
    for post in Post.objects:
        picarray.append(post)
        for x in range(0,len(picarray)):
            path = os.getcwd()+'/polls/static/polls/'+str(picarray[x].image_url)
            file = open(path, 'w+')
            file.write(picarray[x].image.read())
            file.close()
    return picarray

def getImage(path):
    db = connect("mydb")
    for post in Post.objects(image_url=path):
        avgrate = 0
        if (len(post.rate) > 0):
            for rating in post.rate:
                avgrate=avgrate +int(rating.ratings)
            post.avg_rate = avgrate/len(post.rate)
            post.save()
        return post

def updateImage(path,rating,rate_name,comment):
    db = connect("mydb")
    ratinginput = Rating(rating,rate_name,comment)
    ratinginput.save()
    for post in Post.objects(image_url=path):
        post.update(push__rate=ratinginput)
        
def addImage(path,owner,desc):
    db = connect("mydb")
    truepath = path.replace('+','/')                                                                          
    pic = open(truepath)
    image = Post(image_url=path,owner_name=owner,image_desc=desc,avg_rate=-1,rate=[])
    image.image.put(pic)
    image.save()

def backtoIndex():
    return '<html><head><script type="text/javascript">window.location="http://127.0.0.1:8000/polls/";</script></head></html>'

    
def index(request):
    plist = getImages()
    context = {'list': plist}
    return render(request, 'index.html', context)

def detail(request,path):
    post = getImage(path)
    context = {'Post': post}
    return render(request,'detail.html',context)
    
def update(request,path,rating,rate_name,comment):
    updateImage(path,rating,rate_name,comment)
    context = {'Path': path}
    return render(request,'backtoDetail.html',context)

def add(request, path, owner, desc):
    addImage(path,owner,desc)
    plist = getImages()
    context = {'list': plist}
    return HttpResponse(backtoIndex())
    

