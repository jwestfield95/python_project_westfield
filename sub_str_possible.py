mylist='ATTTGGATT'
def sub_str_possible(a_sting_of_letters,k):
        assert k>0,'k cannot by negative'
        assert len (a_string_of_letters) > k, 'length of string is shorter than k'
        possible_sub_str= len(a_sting_of_letters)- k +1
        total_combos= 4**k
        return(min(possible_sub_str,total_combos))
print(sub_str_possible(mylist, -1))
