from rest_framework.decorators import api_view
from rest_framework.response import Response
from game.grade import grade


@api_view(['GET'])
def grade_api(request, which):
    try:
        result = grade(which)
        return Response(result)
    except Exception as e:
        return Response({'message': e.message}, status=400)
