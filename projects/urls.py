from rest_framework import routers
from projects.api import ProjectViewSet

routers = routers.DefaultRouter()

routers.register(r'api/projects', ProjectViewSet, basename='projects')

urlpatterns = routers.urls