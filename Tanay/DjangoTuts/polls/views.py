from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choices
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = 'polls/details.html'
    model = Question

class ResultView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        choice = question.choices_set.get(pk = request.POST['choice'])
    except (KeyError, Choices.DoesNotExist) :
        return render(request, 'details.html', {"question" : question, 'error_message' :"No choice Selected bro"})
    
    else :
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id, )))
