from django.shortcuts import render, get_object_or_404
from .models import Order
from .recommendation import recommend_box


def box_recommendation(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    recommended_box = recommend_box(order)

    return render(
        request,
        'packaging/recommendation.html',
        {
            'order': order,
            'recommended_box': recommended_box,
        }
    )