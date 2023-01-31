from django.conf import settings
from django.urls import path,include
from . import views
# from .views import  SearchResultsView

urlpatterns = [
    path('', views.Map, name = 'map'),
    path('capital', views.StateList, name = 'statelist'),
    path('country/<int:detail_id>/', views.detail, name = 'detail'),
    path('countryinfo/', views.CountryList, name = 'countrylist'),
    path("search/", views.country_list, name="country_list"),
    
    

    ] 

if settings.DEBUG:
    import debug_toolbar 
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns