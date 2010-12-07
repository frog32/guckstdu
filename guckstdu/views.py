from django.shortcuts import render_to_response

def start(request):
    """
    renders the main page
    """
    return render_to_response('start.html', {'user':request.user})