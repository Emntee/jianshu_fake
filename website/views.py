from django.shortcuts import render
from .models import InArticleImage, Article, Comment, CarouselSlide, Collection 
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    options = {
        'collections': Collection.objects.all(),
        'carousel_content': CarouselSlide.objects.all(),
        'notes': Article.objects.all(),
    }
    return render(request, 'website/index.html', options)


def collections(request):
    return HttpResponse("homepage for collections")

def collection(request, collection_id):
    return HttpResponse('will return collection {} homepage'.format(collection_id))

def article(request, article_id):
    return HttpResponse('will return article {} page'.format(article_id)) 

def user_page(request, user_id):
    return HttpResponse('will return homepage of account {}'.format(account_id)) 