from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# My views comes below
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def useLogin(request):
    name = (request.query_params['num'])
    new_num = int(name) * 2
    print(new_num)
    data = {
        "name": "Anthony Chinaemerem",
        "multipliedValue": new_num
        }
    return Response(data)