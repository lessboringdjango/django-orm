from game.system import get_model, get_serializer


def grade_level1(answer):
    Pizza = get_model('Pizza')
    return {
        'count': Pizza.objects.count(),
    }


def grade_level2(answer):
    return {
        'count': answer['count'],
    }


def grade_level3(answer):
    return {
        'exists': answer['exists'],
    }


def grade_level4(answer):
    PizzaSerializer = get_serializer('PizzaSerializer')
    return {
        'pizzas': PizzaSerializer(answer['pizzas'], many=True).data,
    }
