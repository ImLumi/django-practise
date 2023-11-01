from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import TopicSerializer
# from serializers import TopicSerializer
from api.models import Topic

TopicSerializer
@api_view(['GET', 'POST'])
def get_data(req):
    print(req.user)
    if req.method == 'GET':
        topics = Topic.objects.all()
        serialTopic = TopicSerializer(topics, many=True)
        print(serialTopic.data)
        return Response(serialTopic.data)
    elif req.method == 'POST':
        serialTopic = TopicSerializer(data=req.data, context={'request': req})
        serialTopic.is_valid(raise_exception=True)
        serialTopic.save()
        return Response(serialTopic.data)

