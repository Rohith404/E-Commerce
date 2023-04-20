from .models import Cart


def cart_count(request):
    if request.user.is_authenticated:
        cartitems = Cart.objects.filter(user = request.user)
        cart_count = sum(item.quantity for item in cartitems)
    else:
        cart_count = 0
    return{'cart_count' : cart_count}
