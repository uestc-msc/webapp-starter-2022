from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from cards_test.models import Card
from cards_test.serializer import CardSerializer


def hello_world(request):
    return HttpResponse('Hello World!')


def greetings(request, name: str):
    return HttpResponse(f'Hello {name}')


# def listCards(request):
#     cards = Card.objects.all()
#     serialized_cards = CardSerializer(cards, many=True)
#     return HttpResponse(str(serialized_cards.data), content_type='application/json')


# def getCard(request, id: int):
#     card = Card.objects.get(id=id)
#     serialized_card = CardSerializer(card)
#     print(serialized_card.data)
#     return HttpResponse(str(serialized_card.data), content_type='application/json')


# @api_view(['GET'])
# def getCard(request, id: int):
#     card = Card.objects.get(id=id)
#     serialized_card = CardSerializer(card)
#     return Response(serialized_card.data)


class CardListView(ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = 'id'
