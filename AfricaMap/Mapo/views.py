from django.shortcuts import render,get_object_or_404
from Mapo.models import *
# from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
# Create your views here.

def Map(request):
    context = {}
    return render(request, "Africa.html", context)


def CountryList(request):
    countries = Country.objects.all()
    context = {
       'data':countries
      }
    return render(request, "index12.html", context)


def StateList(request):
    state = Country.objects.all().order_by('country')
    context = {
        'state':state
        }
    return render(request, "listing.html", context)


def detail(request, detail_id):
  countries = Country.objects.get(id = detail_id)
#   countries = get_object_or_404(Country, pk=detail_id)
  context = {
      'data':countries
  }
  return render(request, "stateIndex.html", context)


def country_list(request):
  countrys = Country.objects.all()
  country_data = []
  for countries in countrys:
    categories = []
    for category in countries.common_religion.all():
      categories.append(category.name)
    country_data.append(
        {
      'id': countries.id,
      'name': countries.country,
      'population': countries.population,
      'independence date': countries.independence_date,
      'flag': countries.flag.url,
      'categories': categories,
      # Add other country properties here
       })
  return JsonResponse(country_data, safe=False)