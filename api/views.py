from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product
from .serializers import ProductSerializer


# ---------------- PRODUCTS -----------------

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response(serializer.data)


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# ---------------- AUTH: SIGNUP -----------------

@api_view(["POST"])
def signup(request):
    name = request.data.get("name")
    email = request.data.get("email")
    password = request.data.get("password")

    if User.objects.filter(username=email).exists():
        return Response({"error": "User already exists"}, status=400)

    user = User.objects.create(
        username=email,
        first_name=name,
        password=make_password(password)
    )

    return Response({"message": "Signup successful"}, status=200)



# ---------------- AUTH: LOGIN -----------------

@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    # Check user exists
    try:
        user = User.objects.get(username=email)
    except User.DoesNotExist:
        return Response({"error": "Invalid email or password"}, status=400)

    # Validate password
    if not check_password(password, user.password):
        return Response({"error": "Invalid email or password"}, status=400)

    return Response({
        "message": "Login successful",
        "user": {
            "name": user.first_name,
            "email": user.username
        }
    }, status=200)
