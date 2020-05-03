from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from .models import Question
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    latestQuestionsText = Question.objects.order_by('-publicationDate')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latestQuestionsText' : latestQuestionsText,
    }
    return HttpResponse(template.render(context, request))

def getDetails(request,questionId):
    template = loader.get_template('polls/details.html')
    question = get_object_or_404(Question, id=questionId)
    return HttpResponse(template.render({'question':question.questionText},request))

def getResults(request,questionId):
    response = "You are looking at the result for the question %s."
    return HttpResponse(response % questionId)

def vote(request,questionId):
    return HttpResponse("You are voting for the question %s. "%questionId)