"""This is literally to test my testing set up ... """

import pytest
from fbdata import temp


def test_true():
    assert 1 == 1


def test_foo():
    assert temp.foo() == "bar"
