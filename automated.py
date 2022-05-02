#!/usr/bin/env python3

import pandas as pd
def sub_str_possible(a_sting_of_letters,k):#function to get possible substrings
    '''input is a string of letters and k value
        returns minimum possible numbers of substrings'''
    assert k>0,'k cannot by negative'
    possible_sub_str= len(a_sting_of_letters)- k +1
    total_combos= 4**k
    return(min(possible_sub_str,total_combos))
def observed_substrings(string_of_letters,k):#function to get observed substrings
    '''input is a string of letters and k value
    returns number of unique observed substrings'''
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
   
poslist=[]
obslist=[]
kvalues=[]   
def create_df(mylist):#function to get the data frame 3 columns 9 rows, k<10 to match assignment
 
    for k in range(1,len(mylist)):
        '''input is a string of letters
        returns data table of number of unique observed substrings and number of possible substrings for each value of k'''
        obskmers=(observed_substrings(mylist,k))
        obslist.append(obskmers)
    for k in range(1,len(mylist)):
        poskmers=(sub_str_possible(mylist,k))
        poslist.append(poskmers)
    for k in range(1,len(mylist)):
        kvalues.append(k)
    data={'k': kvalues,
        'observed kmers':obslist,
        'possible kmers':poslist}
    df=pd.DataFrame(data)
    return (df)
def Ling_complx(mylist):
    '''input is a string of letters
    returns the sum of number of substrings observed divided by the sum of the number of substrings possible for a specified string'''
    return((sum(obslist))/(sum(poslist)))

myfile='testing.txt'
with open(myfile,"r") as f:
    for line in f:
        print(line)
        print(create_df(line))
        print(Ling_complx(line))
       