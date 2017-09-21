from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Question
from .forms import AskForm, AnswerForm, NewUserForm, LoginForm


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request, *args, **kwargs):
    return render(request, 'question/index.html', {'questions': paginate(request, Question.objects.new()),})


def popular(request, *args, **kwargs):
    return render(request, 'question/index.html', {'questions': paginate(request, Question.objects.popular()),})


def question_details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    form = AnswerForm(initial={'question': question_id})
    return render(request, 'question/details.html', {'question': question, 'form': form})


def question_add(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        import pdb; pdb.set_trace()
        form.instance.author = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'question/add.html', {'form' : form})

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 10:
        limit = 10
    try:
        page = int(request.GET.get('page',1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
