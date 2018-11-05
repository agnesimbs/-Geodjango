from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize
from .models import Counties,Incidences
# Create your views here.
class MapPageView(TemplateView):
	template_name='reporter/index1.html'


def county_datasets(request):
	counties=serialize('geojson',Counties.objects.all())
	return HttpResponse(counties,content_type='json')
def point_datasets(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points,content_type='json')