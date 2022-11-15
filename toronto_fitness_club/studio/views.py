import geopy
import requests

# Create your views here.

# use API for studio page
from geopy import distance

from rest_framework.permissions import IsAuthenticated

# username: thaksha password: water
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from studio.models import GeoProx, Studio, StudioToDistance

# return list with studio id ordered from closest to furthest user can go to
# -> need to store direction to use for link to get direction -> need to
# store as will apply filters on this user get a page where they do filter of
# studios
# enter the studio page they want to go to, then a respose
# is return with the studio id, link to direction, ..
from studio.serializers import GeoProxStudioByCurrentLocationSerializer, \
    GeoProxStudioByPinPointSerializer, \
    GeoProxStudioByPostalSerializer

'https://www.google.com/maps/dir/?api=1&origin={origin_lat},{origin_long}&' \
'destination={dest_lat},{dest_long}&travelmode=driving'


# class StoreView(APIView):
#     def get(self, request, *args, **kwargs):
#         store = get_object_or_404(Store, id=kwargs['store_id'])
#         return Response({
#             'id': store.id,
#             'name': store.name,
#             'description': store.description,
#             'url': store.url,
#             'email': store.email
#         })

# check if dict empty as then they are no studio for user to go to
def calculate_proximity(lat, long):
    # {studio_id: distance to the studio}
    studio_to_distance = {}
    for studio in Studio.objects.all():
        studio_to_distance[studio.id] = distance.geodesic((lat, long), (
            studio.latitude, studio.longitude)).km
        # source for sorting dictionary code "{k: v for k, v in sorted(
        # studio_to_distance.items(), key=lambda item: item[1])}" from
        # https://stackoverflow.com/questions/613183/how-do-i-sort-a
        # -dictionary-by-value

    return {k: v for k, v in
            sorted(studio_to_distance.items(), key=lambda item: item[1])}


# stores this data of {store id: distance} in database so can filter

class GeoProxStudioByCurrentLocation(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GeoProxStudioByCurrentLocationSerializer

    def post(self, request, format=None):
        # use this in get and let user pick a studio id they want to see the
        # page of


        lat = request.data['lat']
        long = request.data['long']

        response = Response()
        response.data = calculate_proximity(lat, long)

        # save user to distance to all studio according to given location to database
        current_user = request.user.id
        if GeoProx.objects.filter(id=current_user):
            GeoProx.objects.get(id=current_user).delete()

        user_to_studio = GeoProx()
        user_to_studio.user_id = current_user
        user_to_studio.save()
        print(response.data)
        for studio_id in response.data.keys():
            studio_to_distance = StudioToDistance()
            studio_to_distance.studio_id = studio_id
            studio_to_distance.distance_to_studio = response.data[studio_id]
            studio_to_distance.save()
            user_to_studio.studio_to_distance.add(studio_to_distance)
            user_to_studio.save()
        print(user_to_studio.studio_to_distance.all())
        for studio in user_to_studio.studio_to_distance.all():
            print(studio.studio_id)

        response.status_code = status.HTTP_200_OK

        return response


class GeoProxStudioByPostal(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GeoProxStudioByPostalSerializer

    def post(self, request, format=None):
        postal_code = request.data["postal_code"].replace(' ', '%')

        # when convert could lead to error if not a valid postal code,
        # validate postal code when user enter before its posted maybe
        # using regex
        # convert postal code to long lat and call calculate_proximity
        # need to validate postal code !!!!!
        geocode_data = requests.get(
            f'https://geocoder.ca/{postal_code}?json=1')
        geodata = geocode_data.json()

        lat = geodata["latt"]
        long = geodata["longt"]

        response = Response()
        response.data = calculate_proximity(lat, long)

        # save user to distance to all studio according to given location to database

        response.status_code = status.HTTP_200_OK

        return response


class GeoProxStudioByPinPoint(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GeoProxStudioByPinPointSerializer

    def post(self, request, format=None):
        lat = request.data["pinpoint_lat"]
        long = request.data["pinpoint_long"]
        calculate_proximity(lat, long)

        # save in database and retrieve last element for this table as that
        # what user last wanted to find the distance
        response = Response()
        response.data = calculate_proximity(lat, long)

        # save user to distance to all studio according to given location to database



        response.status_code = status.HTTP_200_OK

        return response


class FilterStudio(APIView):

    # headers

    def get(self, request, *args, **kwargs):

        prox_user_to_studio = None
        print(f"request id:{request.user.id}")
        for user_to_studio in GeoProx.objects.all():
            if user_to_studio.user_id == str(request.user.id):
                prox_user_to_studio = user_to_studio

        studio_to_distance = {}

        if prox_user_to_studio is not None:
            for studio in prox_user_to_studio.studio_to_distance.all():
               studio_to_distance[studio.studio_id] = studio.distance_to_studio


        # source for sorting dictionary code "{k: v for k, v in sorted(
        # studio_to_distance.items(), key=lambda item: item[1])}" from
        # https://stackoverflow.com/questions/613183/how-do-i-sort-a
        # -dictionary-by-value

        studio_to_distance = {k: v for k, v in
                              sorted(studio_to_distance.items(),
                                     key=lambda item: item[1])}
        response = Response()
        response.data = studio_to_distance
        response.status_code = status.HTTP_200_OK

        return response

    def post(self, request, format=None):
        # filter by name, amenities
        # after get filter by class name  and coaches -> need nitish code


        pass


