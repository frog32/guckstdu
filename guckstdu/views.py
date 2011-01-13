from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from guckstdu.series.models import Series

def start(request):
    """
    renders the main page
    """
    return render_to_response('start.html',{'series':Series.objects.all(),'rec':Series.objects.filter(name__exact='Bored To Death')})
#    return render_to_response('start.html', {'user':request.user})
#start = login_required(start)
