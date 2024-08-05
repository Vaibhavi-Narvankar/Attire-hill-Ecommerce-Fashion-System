from django import template

register = template.Library()


@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
   keys=cart.keys()
   for id in keys:
        if id != 'null' and id.isdigit():  # Check if id is not 'null' and is a valid integer
            if int(id) == product.id:
                return cart.get(id)
   return 0

@register.filter(name='product_total')
def product_total(product,cart):
   return product.price * cart_quantity(product,cart)

@register.filter(name='gst_total')
def gst_total(product,cart):
    gst = 0
    for p in product:
        gst += (6*product_total(p,cart)/100)
    return round(gst, 2)

@register.filter(name='discount')
def discount(product,cart):
    dis = 0
    for p in product:
        dis += (2*product_total(p,cart)/100)
    return round(dis, 2)


@register.filter(name='totat_price')
def totat_price(product,cart):
   sum = 0 
   for p in product:
      sum = sum + (product_total(p,cart)) + (6*product_total(p,cart)/100) - (2*product_total(p,cart)/100)
   return round(sum, 2)