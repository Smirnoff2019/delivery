from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class CommonResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AuthView(APIView):
    """
       User login.
    """

    @swagger_auto_schema(
        request_body=LoginRequestSerializer,
        responses={200: CommonResponseSerializer}
    )
    def post(self, request):
        return Response(CommonResponseSerializer({
            'status': 0,
            'message': 'Thank you for being with us'
        }).data)


@api_view()
def about_us(request):
    return Response({"title": "Будинок іграшок",
                     "description": "«Будинок іграшок» – крупнейшая украинская сеть магазинов игрушек. "
                                    "Наша цель - дарить, удивлять и немножечко дуреть, наполняя жизнь позитивными эмоциями. "
                                    "Мы верим, что взрослых не существует, поэтому ассортимент магазина «Будинок іграшок» настолько широк, что найти подходящую игрушку можно как для новорожденного ребенка, так и для взрослого."})


@api_view()
def contacts(request):
    return Response({
        "title": "Контактна інформація Radio ROKS",
        "description": "Центральний офіс "
                       "04080, Київ, вул. Вікентія Хвойки, 15/15 "
                       "Телефон / факс: +380 (44) 207-39-90 "
                       "Ел. пошта: info@radioroks.ua"})
