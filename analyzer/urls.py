from django.urls import path
from .views import AnalyzeTestView

urlpatterns = [
    path('analyze/', AnalyzeTestView.as_view(), name='analyze'),
]