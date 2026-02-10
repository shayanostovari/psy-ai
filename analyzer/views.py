from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from dotenv import load_dotenv   # ← این رو اضافه کن

from .serializers import TestResultSerializer
from .services.test_engine import run_test

load_dotenv()   # ← این خط رو هم اضافه کن (اگر قبلاً در settings.py لود شده، می‌تونی حذفش کنی)

class AnalyzeTestView(APIView):
    def post(self, request):
        # ────── چک کردن secret ──────
        provided_secret = request.headers.get('X-WP-SECRET')
        expected_secret = os.getenv('WP_SECRET')

        if provided_secret != expected_secret:
            return Response(
                {'error': 'Unauthorized - Invalid secret'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        # ──────────────────────────────

        serializer = TestResultSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = run_test(
            test_code=serializer.validated_data["test_code"],
            answers=serializer.validated_data["answers"],
        )

        return Response(result, status=status.HTTP_200_OK)