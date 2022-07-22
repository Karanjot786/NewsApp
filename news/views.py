from django.shortcuts import render
from .models import Headline
from .getnews.getnews import get_business, get_news, get_indin, get_sports, get_world
import random


def shownews(request):

    get_news()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news.html', context=context)


def shownews1(request):

    get_business()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news1.html', context=context)

def shownews2(request):

    get_indin()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news2.html', context=context)

def shownews3(request):

    get_sports()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news3.html', context=context)


def shownews4(request):

    get_world()

    headlines = Headline.objects.order_by('?')
    preview = []
    right, left = 3, 3

    for head in headlines:
        if head.leaning == 'right' and right > 0 and head.img:
            preview.append(head)
            right -= 1
        elif head.leaning == 'left' and left > 0 and head.img:
            preview.append(head)
            left -= 1

    random.shuffle(preview)
    

    context = {
        'headline_list': headlines,
        'preview': preview,
        'num_headlines': len(headlines) #for debugging purposes
    }
    
    return render(request, 'news/news4.html', context=context)


