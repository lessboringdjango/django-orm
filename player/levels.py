from .models import Pizza, Topping


def level1():
    Pizza.objects.create(name='pepperoni')
    return {}


def level2():
    Pizza.objects.create(name='pepperoni')

    return {
        'count': Pizza.objects.count()
    }


def level3():
    Pizza.objects.create(name='pepperoni')

    return {
        'exists': Pizza.objects.exists()
    }


def level4():
    Pizza.objects.create(name='pepperoni')
    Pizza.objects.create(name='pepperoni')
    Pizza.objects.create(name='pepperoni')
    Pizza.objects.create(name='pepperoni')
    Pizza.objects.create(name='pepperoni')

    return {
        'pizzas': Pizza.objects.all()
    }
