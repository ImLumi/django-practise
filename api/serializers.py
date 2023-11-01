from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from api.models import Topic, Comment


class TopicSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        if not user.is_anonymous:
            print('user: ', user)
            print(validated_data)
            data = validated_data | {'user': user}
            print(data)
            topic = Topic.objects.create(**data)
            return topic
        else:
            print('no user loggin')
            raise

    class Meta:
        model = Topic
        fields = ['name']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
