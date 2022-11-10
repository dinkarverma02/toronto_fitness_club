from django.urls import path

from studio.views import CreateStudioView

app_name = 'Studio'

urlpatterns = [
    path('new/', CreateStudioView.as_view()),
]
