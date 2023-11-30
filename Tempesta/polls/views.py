from django.shortcuts import render

def index(request):
    return render(request, 'polls/index.html')

def poll_of_the_week(request):
    # Load and return the HTML content for Poll of the Week
    return render(request, 'polls/poll_of_the_week.html')

def past_polls(request):
    # Load and return the HTML content for Past Polls
    return render(request, 'polls/past_polls.html')

def signup_login(request):
    # Load and return the HTML content for Signup/Login
    return render(request, 'polls/signup_login.html')
