from unittest import TestCase
from typish._classes import SubscriptableType


class TestSubscriptableType(TestCase):
    def test_subscribing(self):

        class C(metaclass=SubscriptableType):
            ...

        self.assertEqual('arg', C['arg'].__args__)
        self.assertEqual(C, C['arg'].__origin__)

    def test_after_subscription(self):
        class C(metaclass=SubscriptableType):
            @staticmethod
            def _after_subscription(item):
                C.item = item

        C2 = C['arg']
        self.assertEqual('arg', C2.item)
