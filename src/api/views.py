from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import User
from portfolio.models import Project
from .serializers import ProjectSerializer, MessageSerializer


class ProjectView(APIView):
    def get(self, request):
        queryset = Project.objects.all()
        skill = request.query_params.get("skill")
        if skill and skill != "all":
            queryset = queryset.filter(skills__title__iexact=skill).distinct()
        serializer_data = ProjectSerializer(queryset, many=True)
        return Response(serializer_data.data)


class SendMessageView(APIView):
    def post(self, request):
        user = User.objects.filter(is_portfolio=True).last()
        if user is None:
            return Response({"error": "No portfolio user found"}, status=400)
        serializer_data = MessageSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save(user=user)
        return Response({"message": "success"})
