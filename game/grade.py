from player import levels
from game import graders
from markdown import markdown
from game.system import get_model
from game.exceptions import Wrong
import inspect
from django.db import connection


def grade(which):
    try:
        Pizza = get_model('Pizza')
        Pizza.objects.all().delete()
    except:
        pass

    try:
        Topping = get_model('Topping')
        Topping.objects.all().delete()
    except:
        pass

    try:
        grader = getattr(graders, 'grade_level%d' % which)
    except:
        raise Exception('I have not yet made a level %d' % which)

    try:
        level = getattr(levels, 'level%d' % which)
    except:
        raise Exception('Could not find your function level%d(), have you created it in player/levels.py?' % which)

    try:
        initial_query_count = len(connection.queries)
        answer = level()
        queries = connection.queries[initial_query_count:]
        source, _ = inspect.getsourcelines(level)
        source = ' '.join(source)
        grader(source, answer, queries)
        return {'correct': True, 'message': 'WINNER!'}
    except Wrong as e:
        return {'correct': False, 'message': markdown(e.message)}
    except Exception as e:
        return {'correct': False, 'message': e.message}
