from django.urls import path

from . import views



from .views import FilterStudio, GeoProxStudioByCurrentLocation, \
    GeoProxStudioByPinPoint, GeoProxStudioByPostal

app_name = 'Studio'

urlpatterns = [
    path('closest_studio_by_postal/', GeoProxStudioByPostal.as_view()),
    path('closest_studio_by_pinpoint/', GeoProxStudioByPinPoint.as_view()),
    path('closest_studio_by_currentlocation/', GeoProxStudioByCurrentLocation.as_view()),
    path('filter_studio/', FilterStudio.as_view()),
]


# edit studio depends on studio id


