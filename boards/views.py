from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import NewTopicForm
from .models import Board, Topic, Post


def home(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'boards': boards})
	
def services(request):
    boards = Board.objects.all()
    return render(request, 'services.html', {'boards': boards})
	
def about(request):
    boards = Board.objects.all()
    return render(request, 'about.html', {'boards': boards})
	
def portfolio(request):
    boards = Board.objects.all()
    return render(request, 'portfolio.html', {'boards': boards})
	
def contact(request):
    boards = Board.objects.all()
    return render(request, 'contact.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})
