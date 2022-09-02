from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'poll_r_bear_app/poll_r_bear.html', {})