#!/usr/bin/env python3
mylist='ATTTGGATT'
def sub_str_possible(a_sting_of_letters,k):
        assert k>0,'k cannot by negative'
        possible_sub_str= len(a_sting_of_letters)- k +1
        total_combos= 4**k
        return(min(possible_sub_str,total_combos))
print(sub_str_possible(mylist, 4))

import pandas as pd
mylist='ATTTGGATT'
def sub_str_possible(a_sting_of_letters,k):#function to get possible substrings
        assert k>0,'k cannot by negative'
        possible_sub_str= len(a_sting_of_letters)- k +1
        total_combos= 4**k
        return(min(possible_sub_str,total_combos))
def observed_substrings(string_of_letters,k):#function to get observed substrings
    all_substrings= [string_of_letters[i:i+(k)] for i in range(0,len(string_of_letters),1)]
    for i in range(0,len(all_substrings)):
        if(len(all_substrings) ==k):
            all_substrings.pop()
    newlst=[]
    for item in all_substrings:
        if len(item) ==k:
            newlst.append(item) 
    unique_set=set(newlst)
    unique_list=list([unique_set])
    for x in unique_list:
        return (len(x))
o_kmers=[(observed_substrings(mylist,1)),(observed_substrings(mylist,2)),
                            (observed_substrings(mylist,3)),(observed_substrings(mylist,4)),
                            (observed_substrings(mylist,5)),(observed_substrings(mylist,6)),
                            (observed_substrings(mylist,7)),(observed_substrings(mylist,8)), (observed_substrings(mylist,9))]
p_kmers= [(sub_str_possible(mylist,1)),(sub_str_possible(mylist,2)),
                            (sub_str_possible(mylist,3)),(sub_str_possible(mylist,4)),
                            (sub_str_possible(mylist,5)),(sub_str_possible(mylist,6)),
                            (sub_str_possible(mylist,7)),(sub_str_possible(mylist,8)), (sub_str_possible(mylist,9))]
def create_df(mylist):#function to get the data frame 3 columns 9 rows, k<10 to match assignment

    data={'k': [1,2,3,4,5,6,7,8,9],
        'observed kmers':[(observed_substrings(mylist,1)),(observed_substrings(mylist,2)),
                            (observed_substrings(mylist,3)),(observed_substrings(mylist,4)),
                            (observed_substrings(mylist,5)),(observed_substrings(mylist,6)),
                            (observed_substrings(mylist,7)),(observed_substrings(mylist,8)), (observed_substrings(mylist,9))],
        'possible kmers':[(sub_str_possible(mylist,1)),(sub_str_possible(mylist,2)),
                            (sub_str_possible(mylist,3)),(sub_str_possible(mylist,4)),
                            (sub_str_possible(mylist,5)),(sub_str_possible(mylist,6)),
                            (sub_str_possible(mylist,7)),(sub_str_possible(mylist,8)), (sub_str_possible(mylist,9))]}
    df=pd.DataFrame(data)
    return (df)
print(mylist)#curent list being analyzed
print(create_df(mylist))#dataframe for list
print((sum(o_kmers))/(sum(p_kmers)))#linguistic complexity
############################################################################################################################################
import pandas as pd
mylist='ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT'
o_kmers=[(observed_substrings(mylist,1)),(observed_substrings(mylist,2)),
                            (observed_substrings(mylist,3)),(observed_substrings(mylist,4)),
                            (observed_substrings(mylist,5)),(observed_substrings(mylist,6)),
                            (observed_substrings(mylist,7)),(observed_substrings(mylist,8)), (observed_substrings(mylist,9))]
p_kmers= [(sub_str_possible(mylist,1)),(sub_str_possible(mylist,2)),
                            (sub_str_possible(mylist,3)),(sub_str_possible(mylist,4)),
                            (sub_str_possible(mylist,5)),(sub_str_possible(mylist,6)),
                            (sub_str_possible(mylist,7)),(sub_str_possible(mylist,8)), (sub_str_possible(mylist,9))]
def sub_str_possible(a_sting_of_letters,k):#function to get possible substrings
        assert k>0,'k cannot by negative'
        possible_sub_str= len(a_sting_of_letters)- k +1
        total_combos= 4**k
        return(min(possible_sub_str,total_combos))
def observed_substrings(string_of_letters,k):#function to get observed substrings
    all_substrings= [string_of_letters[i:i+(k)] for i in range(0,len(string_of_letters),1)]
    for i in range(0,len(all_substrings)):
        if(len(all_substrings) ==k):
            all_substrings.pop()
    newlst=[]
    for item in all_substrings:
        if len(item) ==k:
            newlst.append(item) 
    unique_set=set(newlst)
    unique_list=list([unique_set])
    for x in unique_list:
        return (len(x))
def create_df(mylist):#function to get the data frame 3 columns 9 rows, k<10 to match assignment

    data={'k': [1,2,3,4,5,6,7,8,9],
        'observed kmers':[(observed_substrings(mylist,1)),(observed_substrings(mylist,2)),
                            (observed_substrings(mylist,3)),(observed_substrings(mylist,4)),
                            (observed_substrings(mylist,5)),(observed_substrings(mylist,6)),
                            (observed_substrings(mylist,7)),(observed_substrings(mylist,8)), (observed_substrings(mylist,9))],
        'possible kmers':[(sub_str_possible(mylist,1)),(sub_str_possible(mylist,2)),
                            (sub_str_possible(mylist,3)),(sub_str_possible(mylist,4)),
                            (sub_str_possible(mylist,5)),(sub_str_possible(mylist,6)),
                            (sub_str_possible(mylist,7)),(sub_str_possible(mylist,8)), (sub_str_possible(mylist,9))]}
    df=pd.DataFrame(data)
    return (df)
print(mylist)#curent list being analyzed
print(create_df(mylist))#dataframe for list
print((sum(o_kmers))/(sum(p_kmers)))#linguistic complexity
############################################################################################################################################
import pandas as pd
mylist='ATATATATATATATATA'
o_kmers=[(observed_substrings(mylist,1)),(observed_substrings(mylist,2)),
                            (observed_substrings(mylist,3)),(observed_substrings(mylist,4)),
                            (observed_substrings(mylist,5)),(observed_substrings(mylist,6)),
                            (observed_substrings(mylist,7)),(observed_substrings(mylist,8)), (observed_substrings(mylist,9))]
p_kmers= [(sub_str_possible(mylist,1)),(sub_str_possible(mylist,2)),
                            (sub_str_possible(mylist,3)),(sub_str_possible(mylist,4)),
                            (sub_str_possible(mylist,5)),(sub_str_possible(mylist,6)),
                            (sub_str_possible(mylist,7)),(sub_str_possible(mylist,8)), (sub_str_possible(mylist,9))]
def sub_str_possible(a_sting_of_letters,k):#function to get possible substrings
        assert k>0,'k cannot by negative'
        possible_sub_str= len(a_sting_of_letters)- k +1
        total_combos= 4**k
        return(min(possible_sub_str,total_combos))
def observed_substrings(string_of_letters,k):#function to get observed substrings
    all_substrings= [string_of_letters[i:i+(k)] for i in range(0,len(string_of_letters),1)]
    for i in range(0,len(all_substrings)):
        if(len(all_substrings) ==k):
            all_substrings.pop()
    newlst=[]
    for item in all_substrings:
        if len(item) ==k:
            newlst.append(item) 
    unique_set=set(newlst)
    unique_list=list([unique_set])
    for x in unique_list:
        return (len(x))
def create_df(mylist):#function to get the data frame 3 columns 9 rows, k<10 to match assignment

    data={'k': [1,2,3,4,5,6,7,8,9],
        'observed kmers':[(observed_substrings(mylist,1)),(observed_substrings(mylist,2)),
                            (observed_substrings(mylist,3)),(observed_substrings(mylist,4)),
                            (observed_substrings(mylist,5)),(observed_substrings(mylist,6)),
                            (observed_substrings(mylist,7)),(observed_substrings(mylist,8)), (observed_substrings(mylist,9))],
        'possible kmers':[(sub_str_possible(mylist,1)),(sub_str_possible(mylist,2)),
                            (sub_str_possible(mylist,3)),(sub_str_possible(mylist,4)),
                            (sub_str_possible(mylist,5)),(sub_str_possible(mylist,6)),
                            (sub_str_possible(mylist,7)),(sub_str_possible(mylist,8)), (sub_str_possible(mylist,9))]}
    df=pd.DataFrame(data)
    return (df)
print(mylist)#curent list being analyzed
print(create_df(mylist))#dataframe for list
print((sum(o_kmers))/(sum(p_kmers)))#linguistic complexity