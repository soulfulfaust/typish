from collections import deque, defaultdict, Set
from typing import (
    Dict,
    List,
    Tuple,
    FrozenSet,
    Deque,
    DefaultDict,
    Type,
    AbstractSet,
    Set as TypingSet
)
from unittest import TestCase
from typish._functions import get_origin, get_alias


class TestOriginAndAlias(TestCase):
    def test_get_origin(self):
        self.assertEqual(list, get_origin(List[int]))
        self.assertEqual(tuple, get_origin(Tuple[int, ...]))
        self.assertEqual(dict, get_origin(Dict[str, int]))
        self.assertEqual(set, get_origin(TypingSet))
        self.assertEqual(deque, get_origin(Deque))
        self.assertEqual(defaultdict, get_origin(DefaultDict))
        self.assertEqual(type, get_origin(Type[int]))
        self.assertEqual(Set, get_origin(AbstractSet))

    def test_get_alias(self):
        self.assertEqual(List, get_alias(list))
        self.assertEqual(Tuple, get_alias(tuple))
        self.assertEqual(Dict, get_alias(dict))
        self.assertEqual(TypingSet, get_alias(set))
        self.assertEqual(FrozenSet, get_alias(frozenset))
        self.assertEqual(Deque, get_alias(deque))
        self.assertEqual(DefaultDict, get_alias(defaultdict))
        self.assertEqual(Type, get_alias(type))
        self.assertEqual(AbstractSet, get_alias(Set))
