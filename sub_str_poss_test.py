#!/usr/bin/env python3
from automated import *

    #observed tests
def test_observed_substring_k_is_9(): #specific test to make sure observed substrings for specific string is correct when k=9
    result=observed_substrings('ATTTGGATT',9)
    expected=1
    assert result==expected
    
def test_obsr_sub_k_is_10():
    result=observed_substrings('ATTTGGATT',10)
    expected=0
    assert result==expected
def test_obs_sub_k_is_14():
    result=observed_substrings('ATATATATATATATATA',14)
    expected=2
    assert result==expected
def test_obs_sub_k_is_30():
    result=observed_substrings('ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT',30)
    expected=26
    assert result==expected
# possible tests
def test_possible_K_is_2():
    result=sub_str_possible('ATTTGGATT',2)
    expected=8
    assert result==expected
    
def test_possible_k_is_7():
    result=sub_str_possible('ATATATATATATATATA',7)
    expected=11
    assert result==expected
def test_possible_k_is_17():
    result=sub_str_possible('ATATATATATATATATA',17)
    expected=1
    assert result==expected
    
#Lingusitc complexity tests
def test_ling_complex():
    result=Ling_complx('ATATATATATATATATA')
    expected=0.2357142857142857
    assert result==expected
def test_ling_complex_2nd_list():
    result=Ling_complx('ATTTGGATT')
    expected=0.875
    assert result==expected

def test_ling_complex_3rd_list():
    result=Ling_complx('ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT')
    expected=0.9738111647139903
    assert result==expected
