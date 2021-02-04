from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
# Create your views here.
from .models import Question, Choice

def index(request):
     # most recent 5 questions, the - is newest first, the [:5] is the number of entries
     latest_question_list = Question.objects.order_by('-pub_date')[:5]
     output = ', '.join([q.question_text for q in latest_question_list])
     # template = loader.get_template('polls/index.html')
     # This dictionary is used to pass information to the front end
     context = {
        'latest_question_list': latest_question_list
     }
     # return HttpResponse(template.render(context,request))
     # render function is a shortcut to avoid using get template loader and then return http response
     return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
      #  question = Question.objects.get(pk=question_id)
    # except:
         # raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', { 'question': question })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))