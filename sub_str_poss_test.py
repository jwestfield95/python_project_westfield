#!/usr/bin/env python3


from sub_str_possbile import *
   
def pos_k():
        assert k>0
from observed_substrings import *

def test_length_k():
    len(observed_substrings) == k
    expected= True 
    assert actual_value== expected 
def test_length_greater():
    len(observed_substrings) > k
    expected= False
    assert actual_value == expected
    
def test_length_lesser():
    len(observed_substrings) < k
    expected= False
    assert actual_value == expected