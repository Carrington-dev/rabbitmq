import json
from django.shortcuts import render
from rest_framework.response import Response
from .producers import producer
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    message = 'not sent'
    try:
        producer.produce(
            exchange='direct', 
            body='Hi there i am alive',
            routing_key='home.cureate_view:0.0.1',
            queue='letterbox'
        )
        message = 'sent'
    except Exception as e:
        message = f'Failed: {e}'

    return Response({
        "message": message
    })