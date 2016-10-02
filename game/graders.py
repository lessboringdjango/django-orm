from game.system import get_model, get_serializer


# Create a single model object
def grade_level1(answer):
    Pizza = get_model('Pizza')
    return {
        'correct': Pizza.objects.count() == 1,
    }


# Count the single model object
def grade_level2(answer):
    return {
        'correct': answer['count'] == 1,
        'count': answer['count'],
    }


# Use exists on the single model object
def grade_level3(answer):
    Pizza = get_model('Pizza')
    return {
        'correct': Pizza.objects.all().exists(),
        'exists': answer['exists'],
    }


# Create at least 5 pizzas and return them all with all
def grade_level4(answer):
    PizzaSerializer = get_serializer('PizzaSerializer')
    return {
        'correct': answer['pizzas'].count() >= 5,
        'pizzas': PizzaSerializer(answer['pizzas'], many=True).data,
    }
