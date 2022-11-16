from django.urls import path

# from classes.views import CreateClassesView, EditClassesView
from . import views
from .views import ClassesView

app_name = 'Classes'

urlpatterns = [
    # path('<int:id>/createclass/', CreateClasses, name="create_classes")
    # path('<int:id>/classes', ListClasses, name="list_classes")
    # path('<str:class>/create_instances/', CreateClassView.as_view()),
    # path('createclasses/', views.ClassesCreate, name="create_classes"),
    # path('<str:pk>/createclass/', views.ClassCreate, name="create_class")
    path('classes-view/', ClassesView.as_view()),
]
