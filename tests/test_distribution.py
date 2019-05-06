import numpy.random
import statlib
import math


x = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4]


def test_h():
    assert statlib.h(x) == {1:3, 2:2, 3:1, 4:5}


def test_f():
    assert statlib.f(x) == {1:3/11, 2:2/11, 3:1/11, 4:5/11}
