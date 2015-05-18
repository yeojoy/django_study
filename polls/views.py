from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.views import generic

# Create your views here.
from django.views.generic import ListView, DetailView

from polls.models import Choice, Question

#logging
import logging
logger = logging.getLogger(__name__)

#--- Class-based GenericView ---#
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(DetailView) :
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(DetailView) :
    model = Question
    template_name = 'polls/results.html'

def vote(request, pk):
    logger.debug("call vote(), with choice's pk, pk is %s", pk)
    p = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        logger.info("finish to vote.")
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

