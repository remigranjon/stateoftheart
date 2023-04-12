from django.db import models
from blog.deletion import SET_WITH
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

domain_choices = (("Chemistry","Chemistry"),
                  ("Environment and Ecology","Environment and Ecology"),
                  ("Physics","Physics"),
                  ( "Biological Sciences","Biological Sciences"),
                  ("Humanities and Social Sciences","Humanities and Social Sciences"),
                  ("Systems Engineering","Systems Engineering"),
                  ("Mathematical Sciences","Mathematical Sciences"),
                  ("Astronomy and Astrophysics","Astronomy and Astrophysics"),
                  ("Earth Sciences","Earth Sciences"),
                  ("Information Sciences","Information Sciences"),
                  ("Nuclear and Particle Physics","Nuclear and Particle Physics"),
                  ("Other","Other"))


class Article(models.Model) :
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    abstract = models.TextField(blank=True)
    publishing_date = models.DateField(default=timezone.now)
    data = models.TextField()
    header_img = models.ImageField(upload_to='headers', blank=True, null=True)
    domain = models.CharField(max_length=250,default = "Other", choices = domain_choices)

    def __str__(self):
        return self.title

class Comment(models.Model) :
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    publishing_date = models.DateTimeField()
    text = models.TextField()
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True, related_name="children",null=True)

class Tag(models.Model) :
    name = models.CharField(max_length=250)
    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.name


# -----------------------Chapter before using Editor.js----------------------

# # getPreviousChapter is a method that connects two chapters that succeeds each other
# # in case of deletion of one Chapter 
# # function to call with on_delete with previous Field
# # the value given is the previous value of the chapter deleted
# def getPreviousChapter(chapter):
#     previous = Chapter.objects.get(id=chapter.previous.id).previous
#     return previous


# # a Chapter is part of an Article, parent Chapter is provided if exists
# # if doesn't exist it's a root Chapter.
# # previous

# class Chapter(models.Model) :
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     title = models.CharField(max_length=250,blank=True)
#     parent = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, related_name="children",null=True)
#     previous = models.ForeignKey('self', blank=True, on_delete=SET_WITH(getPreviousChapter), related_name="next", null=True)
#     text = models.TextField(blank=True)

#     def __str__(self):
#         text = self.title
#         if (self.parent) :
#             text+=" | child of "+ self.parent.title
#         if (self.previous) :
#             text+=" | follows "+ self.previous.title
#         return text
