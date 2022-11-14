from django.urls import path

# from classes.views import CreateClassesView, EditClassesView
from . import views

app_name = 'Classes'

urlpatterns = [
    path('new/', CreateClassesView.as_view()),
    path('<int:classes_id>/', EditClassesView.as_view()),
]
