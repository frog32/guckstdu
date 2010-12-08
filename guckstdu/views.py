from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

def start(request):
    """
    renders the main page
    """
    return render_to_response('start.html', {'user':request.user})
start = login_required(start)