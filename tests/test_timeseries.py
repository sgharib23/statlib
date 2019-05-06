import statlib
from pytest import approx


y = [-6, 1, 0, 7, 9, -3, 3, 10, 1, 10, 8, 7, 6, 6, 5, 15, 13, 16, 12, 22]



def test_moving_avg_5():
    test_value = statlib.moving_avg(y)
    true_value = [None, None, 2.2, 2.8, 3.2, 5.2, 4, 4.2, 6.4, 7.2, 6.4, 7.4, 6.4, 7.8, 9, 11, 12.2, 15.6, None, None]
    assert test_value == approx(true_value, rel = 1e-2)
    
    
def test_moving_avg_3():
    test_value = statlib.moving_avg(y, 3)
    true_value = [None, -1.67, 2.67, 5.33, 4.33, 3, 3.33, 4.67, 7, 6.33, 8.33, 7, 6.33, 5.67, 8.67, 11, 14.67, 13.67, 16.67, None]
    assert test_value == approx(true_value, rel = 1e-2)

    
def test_ols():
    test_value = statlib.ols(y)
    true_value = (-2.31, 0.90)
    assert true_value == approx(test_value, rel=1e-2)
 
