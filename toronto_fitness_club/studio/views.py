import requests

# Create your views here.

# use API for studio page
from geopy import distance
from rest_framework.generics import ListAPIView

from rest_framework.permissions import IsAuthenticated

# username: thaksha password: water
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters, status

from studio.models import Amenities, GeoProx, Studio, StudioToDistance

# return list with studio id ordered from closest to furthest user can go to
# -> need to store direction to use for link to get direction -> need to
# store as will apply filters on this user get a page where they do filter of
# studios
# enter the studio page they want to go to, then a respose
# is return with the studio id, link to direction, ..
from studio.serializers import GeoProxStudioByCurrentLocationSerializer, \
    GeoProxStudioByPinPointSerializer, \
    GeoProxStudioByPostalSerializer, StudioSerializer

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
    all_studios = []
    for studio in Studio.objects.all():
        studio_to_distance = []
        # calculate for each studio the distance to the user

        studio_to_distance.append(studio.id)

        studio_to_distance.append(distance.geodesic((lat, long), (
            studio.latitude, studio.longitude)).km)
        studio_to_distance.append(studio.name)

        all_studios.append(studio_to_distance)




        # source for sorting dictionary code "{k: v for k, v in sorted(
        # studio_to_distance.items(), key=lambda item: item[1])}" from
        # https://stackoverflow.com/questions/613183/how-do-i-sort-a
        # -dictionary-by-value
        # {k: v for k, v in
        # sorted(studio_to_distance.items(), key=lambda item: item[1])}

    return all_studios


# stores this data of {store id: distance} in database so can filter

class GeoProxStudioByCurrentLocation(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GeoProxStudioByCurrentLocationSerializer

    def post(self, request, format=None):
        # use this in get and let user pick a studio id they want to see the
        # page of

        lat = request.data['lat']
        long = request.data['long']

        # [[studio_id, distance, name]]
        studioID_distance_studio = calculate_proximity(lat, long)
        print(studioID_distance_studio)



        #

        # print(studioID_distance_studio[1][1].name)

        # save user to distance to all studio
        # according to given location to database
        current_user = str(request.user.id)
        # delete other call user made to get studio by specific location
        for instance in GeoProx.objects.all():
            if instance.user_id == current_user:
                instance.delete()

        # create a new geoprox object for user
        user_to_studio = GeoProx()
        user_to_studio.user_id = current_user
        user_to_studio.save()

        # Loop through the list 1. create amenties object
        # 2. create StudioToDistance, save it
        # 3. stores in user_to_studio.studio_to_distance

        for studio in studioID_distance_studio:

            studio_obj = StudioToDistance()
            studio_obj.studio_id = studio[0]
            studio_obj.distance_to_studio = studio[1]
            studio_obj.studio_name = studio[2]
            studio_obj.save()
            for item in Amenities.objects.all():
                if item.studios.id == studio[0]:
                    studio_obj.studio_amenities.add(item)

            user_to_studio.studio_to_distance.add(studio_obj)









        # loop through the dictionary that maps studio_id to [distance,
        # studio object] add studio_id, distance and studio_object to a newly
        # create instance of studio_to_distance save the instance of
        # studio_to_distance to the instance of geoprox created above
        # for get query set we call  user_to_studio.studio_to_distance.all()
        # that will return all the studio_to_distance of user
        # create a new model with studio_id, name, amenities, distance
        # when get all studio_to_distance of user it has this form and
        # theres nothing to retreive we can just show this


        """
        for studio in studioID_distance_studio.keys():
            print("in loop")
            studioID_distance_studio[studio] = studioID_distance_studio[studio][
                0]
            studio_to_distance = StudioToDistance()
            studio_to_distance.studio_id = studio
            studio_to_distance.distance_to_studio = \
            studioID_distance_studio[studio][0]
            studio_to_distance.studio_object.add(
                studioID_distance_studio[studio][1])
            studio_to_distance.save()
            print(studio_to_distance.distance_to_studio)
            print(studio_to_distance.studio_object.all())
            user_to_studio.studio_to_distance.add(studio_to_distance)
            user_to_studio.save()
            for thing in user_to_studio.studio_to_distance.all():
                # print(thing.distance_to_studio)
                pass
        """
        response = Response()
        # need to fix
        response.data = {}

        response.status_code = status.HTTP_200_OK

        return response


class SearchStudio(ListAPIView):

    # queryset = Studio.objects.all()
    # pass all studios but list them from
    # closest to furthest as a query set
    # studios listed should only have info such as name and amenities
    # will include class info after...
    serializer_class = StudioSerializer
    filter_backends = [filters.SearchFilter]
    # search includes name and amenities
    search_fields = ['studio_name', 'studio_amenities__type']

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        # make query set with studio but they should be listed from closest to furthest
        # have a model mapping user_id
        # to studio objects that have name, amenenties, other thing.., distance
        # when we get the query we will order by distance
        # the other query set can just store distance from user to each studio
        # which we can use to get long, lat when we give link for direction
        # depending on the studio they clicked.

        # user will click based on up to what they filtered save upto what
        # they filtered to database and retrieve it when we ask them to click
        # for click studio give an api and ask user user to enter the studio
        # id of the one they want to select then from the database we can
        # retreive the studio of the id also get distance from out geoprox
        # model and return a coressponding json response
        # all studio_to_distance_of_user
        geoprox_of_user = GeoProx.objects.get(user_id=str(self.request.user.id))
        print(geoprox_of_user)
        print(geoprox_of_user.studio_to_distance.all())

        return GeoProx.objects.get(
            user_id=str(self.request.user.id)).studio_to_distance.all()


def OrderStudio(user_id: str):
    prox_user_to_studio = None

    for user_to_studio in GeoProx.objects.all():
        if user_to_studio.user_id == user_id:
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
    return studio_to_distance
