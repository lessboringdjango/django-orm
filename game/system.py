from django.apps import apps
from rest_framework import serializers


def get_model(name):
    return apps.get_model('player', name)


def get_serializer(name):
    if name == 'PizzaSerializer':
        Pizza = get_model('Pizza')

        class PizzaSerializer(serializers.ModelSerializer):
            class Meta:
                model = Pizza
                fields = '__all__'
        return PizzaSerializer

    if name == 'ToppingSerializer':
        Topping = get_model('Topping')

        class ToppingSerializer(serializers.ModelSerializer):
            class Meta:
                model = Topping
                fields = '__all__'
        return ToppingSerializer

    raise Exception('Unknown model named ' + name)
