from django.urls import path

from .views import GeoProxStudioByCurrentLocation, \
    GeoProxStudioByPinPoint, GeoProxStudioByPostal, SearchStudio

app_name = 'Studio'

urlpatterns = [
    path('closest_studio_by_CurrentLocation/',
         GeoProxStudioByCurrentLocation.as_view()),
    path('search_studio/', SearchStudio.as_view()),
    path('closest_studio_by_postal/', GeoProxStudioByPostal.as_view()),
    path('closest_studio_by_pinpoint/', GeoProxStudioByPinPoint.as_view()),

]

# edit studio depends on studio id
