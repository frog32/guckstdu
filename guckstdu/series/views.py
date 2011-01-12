from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from series.models import Series
from guckstdu.series.models import Season, Episode

@login_required
@csrf_exempt
def top_series(request):
    return render_to_response('top_series.html', {'series':Series.objects.all()})

@login_required
@csrf_exempt
def series_details(request):
    series = Series.objects.get(id=request.POST.get('series', request.GET.get('series')))
    seasons = Season.objects.filter(series=series)
    return render_to_response('series.html', {'series':series, 'seasons':seasons})

@login_required
@csrf_exempt
def season_details(request):
    season = Season.objects.get(id=request.POST.get('season', request.GET.get('season')))
    episodes = Episode.objects.filter(season=season)
    return render_to_response('season.html', {'season':season, 'episodes':episodes})

@login_required
@csrf_exempt
def episode_details(request):
    episode = Episode.objects.get(id=request.POST.get('episode', request.GET.get('episode')))
    return render_to_response('episode.html', {'episode':episode})