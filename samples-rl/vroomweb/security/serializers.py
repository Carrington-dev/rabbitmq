from rest_framework import serializers

class UserSerializer(serializers.ModelSerialisers):
    class Meta:
        fields = "__all__"