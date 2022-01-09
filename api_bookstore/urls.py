from django.urls import include, path
from rest_framework import routers
from .views import  *


router = routers.DefaultRouter()
router.register(r'Autores',AuthorViewSet)
router.register(r'Libros',BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]