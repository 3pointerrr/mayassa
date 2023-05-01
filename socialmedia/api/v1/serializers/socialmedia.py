from rest_framework import serializers
from socialmedia.models import SocialMedia

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = (
            'title',
            'url',
        )