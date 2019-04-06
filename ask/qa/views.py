from django.http import HttpResponse, Http404
from django.core.paginator import Paginator

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def new(request):
    limit = 10
    page = int(request.GET.get('page', 1))
    paginator = Paginator(Question.objects.new(), limit)
    page = paginator.page(page)
    paginator.baseurl = '/question/'
    return render(request, 'templates/list.html', {
        'paginator': paginator,
        'page':      page.object_list
    })
def popular(request):
    limit = 10
    page = int(request.GET.get(page, 1))
    paginator = Paginator(Question.objects.popular(), limit)
    page = paginator.page(page)
    paginator.baseurl = '/question/'
    return render(request, 'templatese/list.html',{
        'page':      page.object_list,
        'paginator': paginator 

    })
def question(request, num):
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'templates/question.html',{
        'question': q
    })

