from django.shortcuts import render
from .models import EnglishPhrases
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def homepage(request):
    words = EnglishPhrases.objects.order_by('english')
    
    soz = request.GET.get('q', '')
    if soz and soz!='':
        tarjima = EnglishPhrases.objects.filter(english__contains=soz)[:3]
    else:
        tarjima = None 

    p = Paginator(words, 20)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {'page_obj': page_obj, 'q':soz, 'tarjima':tarjima}
    return render(request, 'homepage.html', context)


def word(request, pk):

	form = EnglishPhrases.objects.get(id=pk)

	context = {'form':form}
	return render(request, 'word.html', context)

