from django.contrib import admin
from .models import InArticleImage, Article, Comment, CarouselSlide, Collection, Account 

# Register your models here.
admin.site.register(InArticleImage)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(CarouselSlide)
admin.site.register(Collection)
admin.site.register(Account)
