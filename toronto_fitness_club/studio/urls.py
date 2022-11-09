from django.urls import path

from toronto_fitness_club.studio.views import CreateStudioView

app_name = 'Studio'

urlpatterns = [
    path('new/', CreateStudioView.as_view()),
]
