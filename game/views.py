from rest_framework.decorators import api_view
from rest_framework.response import Response
from game.grade import grade


@api_view(['GET'])
def grade_api(request, which):
    which = int(which)
    try:
        result = grade(which)
        status = 200
    except Exception as e:
        result = {'correct': False, 'message': e.message}
        status = 400

    response = Response(result, status=status)

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
