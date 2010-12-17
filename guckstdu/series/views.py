from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from series.models import Series

def top_series(request):
    return render_to_response('top_series.html', {'series':Series.objects.all()})