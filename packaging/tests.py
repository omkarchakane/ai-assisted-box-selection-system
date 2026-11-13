from decimal import Decimal

from django.test import TestCase

from .models import Product, ShippingBox, Order, OrderItem
from .recommendation import recommend_box


class BoxRecommendationTests(TestCase):

    def setUp(self):

        self.product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

        self.small_box = ShippingBox.objects.create(
            name="Small",
            length=20,
            width=15,
            height=10,
            max_weight=3,
            cost=20
        )

        self.medium_box = ShippingBox.objects.create(
            name="Medium",
            length=35,
            width=25,
            height=10,
            max_weight=5,
            cost=35
        )

        self.large_box = ShippingBox.objects.create(
            name="Large",
            length=45,
            width=35,
            height=20,
            max_weight=10,
            cost=60
        )

        self.order = Order.objects.create(
            order_number="ORD001"
        )

        OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )

    def test_cheapest_suitable_box(self):

        result = recommend_box(self.order)

        self.assertEqual(result, self.medium_box)

    def test_no_box_can_fit_product(self):

        self.small_box.length = 10
        self.small_box.width = 10
        self.small_box.height = 10
        self.small_box.save()

        self.medium_box.length = 10
        self.medium_box.width = 10
        self.medium_box.height = 10
        self.medium_box.save()

        self.large_box.length = 10
        self.large_box.width = 10
        self.large_box.height = 10
        self.large_box.save()

        result = recommend_box(self.order)

        self.assertIsNone(result)

    def test_weight_capacity(self):

        self.small_box.max_weight = Decimal("1")
        self.medium_box.max_weight = Decimal("1")
        self.large_box.max_weight = Decimal("1")

        self.small_box.save()
        self.medium_box.save()
        self.large_box.save()

        result = recommend_box(self.order)

        self.assertIsNone(result)

    def test_empty_order(self):

        empty_order = Order.objects.create(
            order_number="ORD002"
        )

        result = recommend_box(empty_order)

        self.assertIsNone(result)

    def test_product_can_be_rotated(self):

        rotated_product = Product.objects.create(
            name="Rotated Product",
            length=20,
            width=30,
            height=5,
            weight=1
        )

        rotated_order = Order.objects.create(
            order_number="ORD003"
        )

        OrderItem.objects.create(
            order=rotated_order,
            product=rotated_product,
            quantity=1
        )

        result = recommend_box(rotated_order)

        self.assertEqual(result, self.medium_box)