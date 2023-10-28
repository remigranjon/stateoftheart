from django.http import HttpResponse
# Create your views here.
from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from blog.models import Article, Comment, Tag
from .forms import *


import json
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
import os
from django.conf import settings


def home(request) :
    article_list = Article.objects.order_by('-publishing_date')
    if request.user.is_authenticated:
        return render(request, 'blog/home.html', context = {"article_list": article_list, "user": request.user})
    else :
        return render(request, 'blog/home.html', context = {"article_list": article_list})

# class IndexView(generic.ListView):
    
    
#     template_name = "blog/index.html"
#     context_object_name = "article_list"

#     def get_queryset(self):
#         """Return the last five articles published"""
#         return Article.objects.order_by('-publishing_date')
    
#     def get_context_data(self, **kwargs) :
#         context = super(IndexView, self).get_context_data(**kwargs)
#         context['user'] = 
#         return super().get_context_data(**kwargs)

def detail(request, article_id):
    
    article = get_object_or_404(Article, pk=article_id)

   
    class Block :
        def __init__(self,type, data) :
            self.type = type
            if type == "header" :
                self.text = data["text"]
                self.level = data["level"]
            elif type =="paragraph" :
                self.text = data["text"]
            elif type == "image" :
                self.url = data["file"]["url"]
                self.alt = data["caption"]
            elif type == "equation" :
                self.equation = data["equation"]
                self.caption = data["caption"]

    
    rawData = json.loads(article.data)
    data = []
    for rawBlock in rawData["blocks"] :
        data.append(Block(rawBlock["type"], rawBlock["data"]))

    comments = Comment.objects.filter(article=article).order_by("-publishing_date")

    return render(request, 'blog/detail.html', {"article":article, "data":data, "comments":comments, "user": request.user})

def newArticle(request) :
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.method =='POST' :
        form = ArticleForm(request.POST, request.FILES)
    else :
        form = ArticleForm()
    return render(request, 'blog/newArticle.html', {'form' : form})

def saveArticle(request):
    
    if request.method =='POST' :
        if "articleId" in request.POST :
            article = get_object_or_404(Article, pk=request.POST["articleId"])
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid() :
                form.save()
                # article = get_object_or_404(Article, pk=request.POST["articleId"])
                if article.header_img == None or not article.header_img:
                    if article.domain == "Chemistry" :
                        article.header_img = "domains/chemistry.jpg"
                    elif article.domain == "Environment and Ecology" :
                        article.header_img = "domains/ecology.jpg"
                    elif article.domain == "Physics" :
                        article.header_img = "domains/physics.jpg"
                article.save()

                article.tag_set.clear()

                if request.POST["tags"] != " " :
                    tags = request.POST["tags"].split(" ");
                    del tags[0]
                    tags.pop()
                    if len(tags)!=0 :
                        for tag in tags :
                            normalTag = tag.lower()
                            if len(Tag.objects.filter(name=normalTag)) > 0  :
                                Tag.objects.get(name=normalTag).articles.add(article)
                            else :
                                newTag = Tag(name=normalTag)
                                newTag.save()
                                newTag.articles.add(article)

                
                return render(request, 'blog/articleSaved.html', context={
                "POST" : json.dumps(request.POST), "article": article,
                })

 
            else :
                return render(request, 'blog/articleSaved.html', context={"error":form.errors})

        else :
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid() :
                
                article = form.save(commit=False)
                article.author = request.user
                if article.header_img == None or not article.header_img:
                    if article.domain == "Chemistry" :
                        article.header_img = "domains/chemistry.jpg"
                    elif article.domain == "Environment and Ecology" :
                        article.header_img = "domains/ecology.jpg"
                    elif article.domain == "Physics" :
                        article.header_img = "domains/physics.jpg"
                article.save()

                if request.POST["tags"] != " " :
                    tags = request.POST["tags"].split(" ");
                    del tags[0]
                    tags.pop()
                    if len(tags)!=0 :
                        for tag in tags :
                            normalTag = tag.lower()
                            if len(Tag.objects.filter(name=normalTag)) > 0  :
                                Tag.objects.get(name=normalTag).articles.add(article)
                            else :
                                newTag = Tag(name=normalTag)
                                newTag.save()
                                newTag.articles.add(article)

                return render(request, 'blog/articleSaved.html', context={
                    "POST" : json.dumps(request.POST), 
                    "article": article,
                    })  
            else :
                return render(request, 'blog/articleSaved.html', context={"error":form.errors})

    # if "articleId" in request.POST :
    #     article = get_object_or_404(Article, pk=request.POST["articleId"])
    #     article.title = request.POST["articleTitle"]
    #     article.abstract = request.POST["articleAbstract"]
    #     article.data = request.POST["articleData"]
    #     article.save()

    # else :
    #     newArticle = Article(
    #         title = request.POST["articleTitle"],
    #         abstract = request.POST["articleAbstract"],
    #         publishing_date = timezone.now(),
    #         data = request.POST["articleData"]
    #     )
    #     newArticle.save()

    
def updateArticle(request, article_id) :
    article = get_object_or_404(Article, pk=article_id)
    form = ArticleForm(instance=article)
    tagsToAdd = ""

    for tag in article.tag_set.all() :
        tagsToAdd += tag.name+" "

    return render(request, 'blog/updateArticle.html', {
        "article":article,
        "form":form,
        "tagsToAdd":tagsToAdd,
        })

def deleteArticle(request, article_id) :
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return redirect("blog:home")

@csrf_exempt
def uploadImage(request):
    if request.method == 'POST':
        # Accéder au contenu du champ image
        imageData = request.FILES['image'].read()

        image = Image.open(BytesIO(imageData))

        image_name = request.FILES['image'].name

        relative_path = "articlesContent/" + image_name

        absolute_path = os.path.join(settings.MEDIA_ROOT, relative_path)

        image.save(absolute_path, 'JPEG')

        absolute_url = settings.MEDIA_URL + relative_path
       
        response = { "success" : 1,
        "file": {
            "url" : absolute_url,
            "relativeUrl" : relative_path
                  
        }
        }

        return HttpResponse(json.dumps(response), content_type="application/json",)
    else:
        response = {
            "success": 0,
            "message": "An error occurred while uploading the image"
        }
        return HttpResponse(json.dumps(response), content_type="application/json")
    
    
    
def writeComment(request, article_id) :
    
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
    article = get_object_or_404(Article, pk=article_id)

    # Ajout du commentaire dans la base de donnée si un nouveau commentaire est posté
    
    if request.method == "POST" :
        if request.user.is_authenticated :
            newComment = Comment(
                author = request.user,
                article = article,
                publishing_date = timezone.now(),
                text = request.POST["comment_text"])
            if "comment_parent" in request.POST :
                newComment.parent = Comment.objects.get(pk=request.POST["comment_parent"])
            newComment.save()

    return redirect("blog:detail", article_id = article_id)

def deleteComment(request) :
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
    if request.method == 'POST' :
        commentToDelete = Comment.objects.get(pk=request.POST["commentId"])
        commentToDelete.delete()
        articleId = int(request.POST["articleId"])
        return redirect("blog:detail", article_id = articleId)

def searchArticle(request) :
       
    if request.method == 'POST' :
        tags = request.POST["queryText"].lower().split(" ")
        tagsString = '+'.join(tags)

        if request.POST["querySettings"]=="byTag" :
            forcounter = 0
            for tag in tags :
                if forcounter==0 :
                    referenceArticleList = Tag.objects.get(name=tag).articles.all()
                elif forcounter > 0 :
                    newArticleList = Tag.objects.get(name=tag).articles.all()
                    set1 = set(referenceArticleList)
                    set2 = set(newArticleList)
                    referenceArticleList = list(set1 & set2)

                forcounter += 1
            return render(request, "blog/results.html", {"articleList":referenceArticleList, "tags":tags, "tagsString": tagsString})

        elif request.POST["querySettings"]=="byTitle" :
            forcounter = 0
            for tag in tags :
                if forcounter==0 :
                    referenceArticleList = Article.objects.filter(title__contains=tag)
                elif forcounter > 0 :
                    newArticleList = Article.objects.filter(title__contains=tag)
                    set1 = set(referenceArticleList)
                    set2 = set(newArticleList)
                    referenceArticleList = list(set1 & set2)

                forcounter += 1
            return render(request, "blog/results.html", {"articleList":referenceArticleList, "tags":tags, "tagsString": tagsString})


        # if request.POST["querySettings"]=="byTag" :
        #     articleList = Article.objects.filter(tag__name__in = tags).distinct().order_by('-publishing_date')
        #     return render(request, "blog/results.html", {"articleList":articleList, "tags":tags, "tagsString": tagsString})
        # elif request.POST["querySettings"]=="byTitle" :
        #     articleList
