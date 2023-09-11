from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Newsletter
from .serializers import NewsletterSerializer

@api_view(['POST'])
def post_create_view(request):
    if request.method == 'POST':
        serializer = NewsletterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Add the Access-Control-Allow-Origin header to allow requests from any origin
            response = Response(serializer.data, status=201)
            response["Access-Control-Allow-Origin"] = "*"  # Replace with your desired origin
            return response
        return Response(serializer.errors, status=400)
    
@api_view(['OPTIONS'])
def handle_preflight(request):
    response = Response()
    response["Access-Control-Allow-Origin"] = "http://127.0.0.1:3000"  # Replace with your React app's origin
    response["Access-Control-Allow-Methods"] = "POST, OPTIONS"  # Include the allowed HTTP methods
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"  # Include any required headers
    response["Access-Control-Allow-Credentials"] = "true"  # Allow credentials (cookies)
    return response


