from game.system import get_model
from django.conf import settings
from game.exceptions import Wrong


def assert_player_app_installed():
    if 'player' not in settings.INSTALLED_APPS:
        raise Wrong('Could not find your app `player`.  Is it listed in `INSTALLED_APPS`?')


def assert_pizza_model_exists():
    if get_model('Pizza') is None:
        raise Wrong('Could not find your model `Pizza`.')


def assert_name_field_exists_on_pizza():
    if 'name' not in [
        f.name
        for f in get_model('Pizza')._meta.get_fields()
    ]:
        raise Wrong('Could not find a `name` field on `Pizza`.')


# Set up the project
def grade_level1(source, answer, queries):
    pass


# Create an app called 'player'
def grade_level2(source, answer, queries):
    assert_player_app_installed()


# Create a model called Pizza
def grade_level3(source, answer, queries):
    assert_player_app_installed()
    assert_pizza_model_exists()


# Add a name field to Pizza
def grade_level4(source, answer, queries):
    assert_player_app_installed()
    assert_pizza_model_exists()
    assert_name_field_exists_on_pizza()


# Create an instance of Pizza without create
def grade_level5(source, answer, queries):
    assert_player_app_installed()
    assert_pizza_model_exists()
    assert_name_field_exists_on_pizza()
    Pizza = get_model('Pizza')

    if 'create' in source:
        raise Wrong("Don't use create yet!  Are you reading ahead?")

    if Pizza.objects.count() != 1:
        raise Wrong('There are no `Pizza`s in the database.  Did you forget to `save()` the instance?')


# Create an instance of Pizza with create
def grade_level6(source, answer, queries):
    assert_player_app_installed()
    assert_pizza_model_exists()
    assert_name_field_exists_on_pizza()
    Pizza = get_model('Pizza')

    if 'create' not in source:
        raise Wrong("You will need to use the `create()` method.")

    if 'save' in source:
        raise Wrong('Use the `create()` method to create a model instance without using the `save()` method.')

    if Pizza.objects.count() != 1:
        raise Wrong('There are no `Pizza`s in the database.  Did you forget to `save()` the instance?')


# count()
def grade_level7(source, answer, queries):
    assert_player_app_installed()
    assert_pizza_model_exists()
    assert_name_field_exists_on_pizza()
    Pizza = get_model('Pizza')

    if not any('SELECT COUNT' in q['sql'] for q in queries):
        raise Wrong('Did you call `count()` on your list?')

    if Pizza.objects.count() != 1:
        raise Wrong('Did you create a `Pizza` before counting?')
