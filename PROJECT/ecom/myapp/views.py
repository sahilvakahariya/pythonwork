from django.shortcuts import render
from rest_framework import viewsets
from myapp.serializer import *
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.response import Response
from rest_framework import status
import razorpay
import random

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
    

class AddressViewSet(viewsets.ModelViewSet):


    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """
        Return only addresses belonging to logged-in user.
        """
        return Address.objects.filter(
            user=self.request.user
        ).order_by("-is_default", "-created_at")
        
        
    def perform_create(self, serializer):
        """
        Automatically assign logged-in user.
        User does not need to send user ID.
        """
        serializer.save(
            user=self.request.user
        )
        
        
class CartViewSet(APIView):
    
    def get_cart(self,user):
        cart,created = Cart.objects.get_or_create(user=user)  
        return cart
    
    def get(self,request):
        cart = Cart.objects.get(user=request.user)
        serializer = CartSerializer(cart)

        return Response(
                    {
                        
                        "cart": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
    
    def post(self,request):
        data = request.data
        product = data['product']
        qty = data['qty']
        
        try:

            product = Product.objects.get(
                id=product,
                is_active=True
            )

        except Product.DoesNotExist:

            return Response(
                {
                    "error": "Product not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
        cart = self.get_cart(request.user)
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product= product,
            defaults={
                "quantity": qty
            }
        )
        
        
        if not created:
            new_quantity = (
                cart_item.quantity + qty
            )
        
            cart_item.quantity = new_quantity

            cart_item.save()
           
        serializer = CartSerializer(
            cart
        )

        return Response(
            {
                "message": "Product added to cart successfully.",
                "cart": serializer.data
            },
            status=status.HTTP_200_OK
        )
       
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def payment(request):
    amount = request.data['amount']
    id = "rzp_test_TOqCWmcFFPZQOB"
    secret="Hhm19s6HIdJkH3Huv8qWHZcd"

    client = razorpay.Client(auth=(id,secret))

    data = { "amount": amount*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    print(payment)
    return Response(payment)   


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def confirmorder(request):

    user = request.user

    print("====================================")
    print("CONFIRM ORDER")
    print("USER:", user)
    print("DATA:", request.data)


    # ========================================================
    # 1. GET DEFAULT ADDRESS
    # ========================================================

    address = Address.objects.filter(
        user=user,
        is_default=True
    ).order_by(
        "-created_at"
    ).first()


    # ========================================================
    # 2. IF DEFAULT ADDRESS NOT FOUND
    # USE LATEST ADDRESS
    # ========================================================

    if not address:

        address = Address.objects.filter(
            user=user
        ).order_by(
            "-created_at"
        ).first()


    # ========================================================
    # 3. IF NO ADDRESS AT ALL
    # ========================================================

    if not address:

        return Response(
            {
                "success": False,
                "error": "No address found.",
                "message": (
                    "Please add a delivery address "
                    "before placing the order."
                )
            },
            status=status.HTTP_400_BAD_REQUEST
        )


    # ========================================================
    # 4. GET CART
    # ========================================================

    try:

        cart = Cart.objects.get(
            user=user
        )

    except Cart.DoesNotExist:

        return Response(
            {
                "success": False,
                "error": "Cart not found.",
                "message": "Please add products to cart first."
            },
            status=status.HTTP_400_BAD_REQUEST
        )


    # ========================================================
    # 5. GET CART ITEMS
    # ========================================================

    items = cart.items.select_related(
        "product"
    ).all()


    if not items.exists():

        return Response(
            {
                "success": False,
                "error": "Cart is empty.",
                "message": "Please add products to cart first."
            },
            status=status.HTTP_400_BAD_REQUEST
        )


    # ========================================================
    # 6. PAYMENT DATA
    # ========================================================

    payment_method = request.data.get(
        "payment_method",
        "COD"
    )

    transaction_id = request.data.get(
        "transaction_id"
    )

    amount = request.data.get(
        "amount"
    )


    # ========================================================
    # 7. PAYMENT METHOD
    # ========================================================

    payment_method = str(
        payment_method
    ).upper().strip()


    valid_methods = [
        "COD",
        "CARD",
        "UPI",
        "NET_BANKING"
    ]


    if payment_method not in valid_methods:

        return Response(
            {
                "success": False,
                "error": "Invalid payment method.",
                "received": payment_method,
                "allowed": valid_methods
            },
            status=status.HTTP_400_BAD_REQUEST
        )


    # ========================================================
    # 8. TOTAL AMOUNT
    # ========================================================

    total_amount = cart.total_amount


    # ========================================================
    # 9. AMOUNT VALIDATION
    # ========================================================

    if amount in [None, ""]:

        amount = total_amount

    else:

        try:

            amount = float(amount)

        except (ValueError, TypeError):

            return Response(
                {
                    "success": False,
                    "error": "Invalid amount."
                },
                status=status.HTTP_400_BAD_REQUEST
            )


        if abs(
            float(total_amount) - amount
        ) > 0.01:

            return Response(
                {
                    "success": False,
                    "error": "Amount does not match cart total.",
                    "cart_total": str(total_amount),
                    "received_amount": str(amount)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


    # ========================================================
    # 10. CHECK STOCK
    # ========================================================

    for item in items:

        if item.quantity > item.product.quantity:

            return Response(
                {
                    "success": False,
                    "error": "Not enough stock.",
                    "product": item.product.name,
                    "available": item.product.quantity,
                    "requested": item.quantity
                },
                status=status.HTTP_400_BAD_REQUEST
            )


    # ========================================================
    # 11. CREATE UNIQUE ORDER NUMBER
    # ========================================================

    order_number = (
        f"ORDER-{random.randint(100000, 999999)}"
    )


    while Order.objects.filter(
        order_number=order_number
    ).exists():

        order_number = (
            f"ORDER-{random.randint(100000, 999999)}"
        )


    # ========================================================
    # 12. CREATE ORDER
    # ========================================================

    try:

        order = Order.objects.create(

            user=user,

            address=address,

            order_number=order_number,

            total_amount=total_amount,

            status=Order.Status.PENDING
        )

    except Exception as e:

        print(
            "ORDER ERROR:",
            str(e)
        )

        return Response(
            {
                "success": False,
                "error": "Order creation failed.",
                "details": str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


    # ========================================================
    # 13. CREATE ORDER ITEMS
    # ========================================================

    try:

        for item in items:

            subtotal = (
                item.product.price *
                item.quantity
            )


            OrderItem.objects.create(

                order=order,

                product=item.product,

                product_name=item.product.name,

                price=item.product.price,

                quantity=item.quantity,

                subtotal=subtotal
            )

    except Exception as e:

        order.delete()

        print(
            "ORDER ITEM ERROR:",
            str(e)
        )

        return Response(
            {
                "success": False,
                "error": "Order item creation failed.",
                "details": str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


    # ========================================================
    # 14. PAYMENT STATUS
    # ========================================================

    if payment_method == "COD":

        payment_status = Payment.Status.PENDING

    else:

        payment_status = Payment.Status.SUCCESS


    # ========================================================
    # 15. CREATE PAYMENT
    # ========================================================

    try:

        Payment.objects.create(

            order=order,

            transaction_id=transaction_id,

            amount=total_amount,

            payment_method=payment_method,

            status=payment_status
        )

    except Exception as e:

        order.delete()

        print(
            "PAYMENT ERROR:",
            str(e)
        )

        return Response(
            {
                "success": False,
                "error": "Payment creation failed.",
                "details": str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


    # ========================================================
    # 16. REDUCE STOCK
    # ========================================================

    for item in items:

        product = item.product

        product.quantity -= item.quantity

        product.save(
            update_fields=[
                "quantity"
            ]
        )


    # ========================================================
    # 17. CLEAR CART
    # ========================================================

    items.delete()


    # ========================================================
    # 18. SUCCESS RESPONSE
    # ========================================================

    print(
        "ORDER CREATED:",
        order.order_number
    )

    print(
        "===================================="
    )


    return Response(
        {
            "success": True,

            "message": "Order placed successfully.",

            "order_number": (
                order.order_number
            ),

            "total_amount": str(
                order.total_amount
            ),

            "payment_method": (
                payment_method
            ),

            "payment_status": (
                payment_status
            ),

            "address": {

                "full_name": (
                    address.full_name
                ),

                "phone": (
                    address.phone
                ),

                "address_line": (
                    address.address_line
                ),

                "city": (
                    address.city
                ),

                "state": (
                    address.state
                ),

                "country": (
                    address.country
                ),

                "pincode": (
                    address.pincode
                )
            }
        },

        status=status.HTTP_201_CREATED
    )



@api_view(['GET'])
def myorders(request):
    orders = Order.objects.get(user=request.user)
    ser = OrderSerializer(orders)
    return Response({"orders":ser.data})