from rest_framework.decorators import api_view
from rest_framework.response import Response

# My views comes below
@api_view()
def login(request):
    data = "Hello"
    return Response(data)