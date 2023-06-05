from models import Project
from rest_framework import viewsets,permissions

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes =  [ ]