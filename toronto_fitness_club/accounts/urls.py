from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import RegisterAPIView, LoginAPIView, UserInfoAPIView, UpdateInfoAPIView, LogoutAPIView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('user/info', UserInfoAPIView.as_view(), name='info'),
    path('user/update', UpdateInfoAPIView.as_view(), name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
