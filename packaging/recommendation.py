from decimal import Decimal

def product_fits_in_box(product, box):

    product_dimensions = sorted([
        product.length,
        product.width, 
        product.height
    ])

    box_dimensions = sorted([
        box.length,
        box.width,
        box.height
    ])

    return all(
        product_dimension <= box_dimension
        for product_dimension, box_dimension
        in zip(product_dimensions, box_dimensions)
    )


def recommend_box(order):
    items = order.items.select_related('product')

    if not items.exists():
        return None

    total_weight = Decimal("0")
    total_volume = Decimal("0")
    products = []

    for item in items:
        product = item.product
        quantity = item.quantity

        total_weight += product.weight * quantity

        product_volume = (
            product.length *
            product.width *
            product.height
        )

        total_volume += product_volume * quantity

        products.append(product)

    suitable_boxes = []

    from .models import ShippingBox

    for box in ShippingBox.objects.all():

        if total_weight > box.max_weight:
            continue

        if total_volume > (
            box.length * box.width * box.height
        ):
            continue

        if not all(
            product_fits_in_box(product, box)
            for product in products
        ):
            continue

        suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    return min(
        suitable_boxes,
        key=lambda box: (box.cost, box.pk)
    )