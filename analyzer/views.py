from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TestResultSerializer
from .services.test_engine import run_test

class AnalyzeTestView(APIView):
    def post(self, request):
        serializer = TestResultSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = run_test(
            test_code=serializer.validated_data["test_code"],
            answers=serializer.validated_data["answers"],
        )

        return Response(result, status=status.HTTP_200_OK)
