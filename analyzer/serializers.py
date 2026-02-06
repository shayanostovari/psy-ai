from rest_framework import serializers

class TestResultSerializer(serializers.Serializer):
    test_code = serializers.CharField(max_length=50)
    answers = serializers.DictField(
        child=serializers.IntegerField(min_value=0, max_value=5)
    )
