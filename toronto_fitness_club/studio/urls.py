from django.urls import path

from .views import FilterStudio, GeoProxStudioByCurrentLocation, \
    SearchStudio

app_name = 'Studio'

urlpatterns = [
    path('closest_studio_by_CurrentLocation/',
         GeoProxStudioByCurrentLocation.as_view()),
    path('search_studio/', SearchStudio.as_view()),
    path('filter_studio/', FilterStudio.as_view()),
]

# edit studio depends on studio id
