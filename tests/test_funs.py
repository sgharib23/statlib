import numpy.random
import numpy
import statlib
from pytest import approx



x = numpy.random.normal(size=100)
y = 2+0.9*x+numpy.random.normal(size=100)


def test_max():
    assert statlib.max(x) == max(x)


def test_min():
    assert statlib.min(x) == min(x)


def test_sum():
    assert statlib.sum(x) == sum(x)


def test_mean():
    test_value = statlib.mean(x)
    true_value = numpy.mean(x)
    assert true_value == approx(test_value, rel=1e-4)


def test_var():
    test_value = statlib.var(x)
    true_value = numpy.var(x)
    assert true_value == approx(test_value, rel=1e-4)


def test_sd():
    test_value = statlib.sd(x)
    true_value = numpy.std(x)
    assert true_value == approx(test_value, rel=1e-4)


def test_range():
    test_value = statlib.range(x)
    true_value = max(x)-min(x)
    assert true_value == approx(test_value, rel=1e-4)


def test_median():
    test_value = statlib.median(x)
    true_value = numpy.median(x)
    assert true_value == approx(test_value, rel=1e-4)


def test_cov():
    test_value = statlib.cov(x, y)
    true_value = numpy.cov(x, y)[0][1]
    assert true_value == approx(test_value, rel=1e-4)


def test_cor():
    test_value = statlib.cor(x, y)
    true_value = numpy.corrcoef(x, y)[0][1]
    assert true_value == approx(test_value, rel=1e-4)
