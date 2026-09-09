from src.calculator.core import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(1,2)==3

def test_sub():
    assert subtract(5,3)==2

def test_mul():
    assert multiply(4,6)==24

def test_div():
    assert divide(8,2)==4

def test_div_zero():
    try:
        divide(1,0)
        assert False
    except ZeroDivisionError:
        pass
