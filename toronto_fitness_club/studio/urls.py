from django.urls import path

from studio.views import CreateStudioView, DeleteStudio, EditStudioView

app_name = 'Studio'

urlpatterns = [
    path('new/', CreateStudioView.as_view()),
    path('<int:studio_id>/', EditStudioView.as_view()),
    path('delete/<int:studio_id>/', DeleteStudio.as_view()),
]

# edit studio depends on studio id
