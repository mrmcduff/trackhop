from tools import volatility_tools as vt
import pytest

def test_sum_squares():
  ans = vt.sum_squares([1, 2, 3, 4])
  assert ans == 1+4+9+16

def test_sum_squared():
  ans = vt.sum_squared([1, 2, 3, 4, 5])
  assert ans == 15**2

def test_validate_valids():
  assert vt.validate_numbers([1, 3, 777777, 4e7, 0.000122, 1e-3])

def test_validate_negatives():
  with pytest.raises(ValueError):
    vt.validate_numbers([1, 3, -2])

def test_validate_zeros():
  with pytest.raises(ValueError):
    vt.validate_numbers([55, 1e4, 0, 12])

def test_get_uis_length():
  uis = vt.get_uis([2, 3, 4, 5])
  assert len(uis) == 3
  assert min(uis) > 0

def test_validate_valid_keys():
  test_list = [{ 'a': 1, 'b': 2}, { 'a': 'foo', 'x': 13, 'c': 12}]
  test_list_with_c =  [{ 'a': 1, 'c': 2}, { 'a': 'foo', 'c': 13}]
  assert vt.validate_key(test_list, 'a') is True
  assert vt.validate_key(test_list, 'x') is False
  assert vt.validate_key(test_list_with_c, 'c') is True
