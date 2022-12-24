from django.shortcuts import render,get_object_or_404
from Mapo.models import *
from django.views.generic import TemplateView, ListView
from django.db.models import Q 
# Create your views here.

def Map(request):
    context = {}
    return render(request, "Africa.html", context)


def CountryList(request):
    countries = Country.objects.all()
    context = {
        'data':countries
        }
    return render(request, "ikeoluwa.html", context)


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


class SearchResultsView(ListView):
    model = City
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Country.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list