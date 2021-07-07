from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreatePollForm
from .models import Poll

def index(request):
    polls = Poll.objects.all()
    return render(request,'poll/index.html',{'polls' : polls})

def test(request):
    polls = Poll.objects.all()
    return render(request,'poll/test.html',{'polls' : polls})

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'poll/create.html', context)

def check(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.answer = poll.option_one
        elif selected_option == 'option2':
            poll.answer = poll.option_two
        elif selected_option == 'option3':
            poll.answer = poll.option_three
        elif selected_option == 'option4':
            poll.answer = poll.option_four
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()
    
    return redirect('index')

def result(request):
	polls = Poll.objects.all()

	return render(request,'poll/result.html',{'polls':polls})

def clear(request):
    polls = Poll.objects.all().delete()

    return redirect('index')

