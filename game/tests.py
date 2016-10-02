from rest_framework.decorators import api_view
from . import levels
from . import grader

# receive request from client
# get the level object
# run it
# return response as json


@api_view
def run_level(request, which):
    level = getattr(levels, 'level' + which)
    grade = getattr(grader, 'grade_level' + which)
    result = grade(level())
    print result
