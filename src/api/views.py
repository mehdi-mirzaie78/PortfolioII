from rest_framework.response import Response
from rest_framework.views import APIView
from portfolio.models import Project
from .serializers import ProjectSerializer


class ProjectView(APIView):
    def get(self, request):
        queryset = Project.objects.all()
        skill = request.query_params.get("skill")
        if skill and skill != "all":
            queryset = queryset.filter(skills__title__iexact=skill).distinct()

            print(queryset)
        serializer_data = ProjectSerializer(queryset, many=True)
        return Response(serializer_data.data)
