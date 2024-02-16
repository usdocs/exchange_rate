from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from currency.models import Currency
from currency.serializers import CurrencySerializer


@api_view(['GET'])
def rate_view(request):
    if ('charcode' not in request.GET or 'date' not in request.GET):
        return Response(
            {'Отсутствуют обязательные параметры "charcode" и "date"'},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        currency = Currency.objects.get(
            charcode=request.GET.get('charcode'),
            date=request.GET.get('date')
        )
    except Exception:
        return Response(
            {'Отсутствует курс валюты на заданную дату'},
            status=status.HTTP_400_BAD_REQUEST
        )
    serializer = CurrencySerializer(currency)
    return Response(serializer.data, status=status.HTTP_200_OK)
