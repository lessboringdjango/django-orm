from player import levels
from game import graders
from game.system import get_model


def grade(which):
    try:
        Pizza = get_model('Pizza')
        Topping = get_model('Topping')
    except:
        raise Exception('Could not find models Pizza and Topping')

    Topping.objects.all().delete()
    Pizza.objects.all().delete()

    try:
        grader = getattr(graders, 'grade_level%s' % which)
    except:
        raise Exception('I have not yet made a level %s' % which)

    try:
        level = getattr(levels, 'level%s' % which)
    except:
        raise Exception('Could not find your function level%s(), have you created it in player/levels.py?')

    try:
        result = grader(level())
    except Exception as e:
        raise Exception('Problem running level: %s' % e.message)

    return result
