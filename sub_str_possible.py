#!/usr/bin/env python3


import pandas as pd
mylist='ATTTGGATT'
def sub_str_possible(a_sting_of_letters,k):#function to get possible substrings
    '''input is a string of letters and k value
        returns minimum possible numbers of substrings'''
    assert k>0,'k cannot by negative'
    possible_sub_str= len(a_sting_of_letters)- k +1 #takes the length of the string -k +1 and prints possible substrings
    total_combos= 4**k #prints the number of total combinations with a four letter alphabet
    return(min(possible_sub_str,total_combos))#prints the minimum number between possible substrings and total combinations for specified k value

def observed_substrings(string_of_letters,k):#function to get observed substrings
    '''input is a string of letters and k value
    returns number of unique observed substrings'''
    assert k>0,'k cannot by negative'
    all_substrings= [string_of_letters[i:i+(k)] for i in range(0,len(string_of_letters),1)]#take a group of letters based on k starting with first letter and moving through each of the characters in the string (if k=2 and string is 'abcd', get 'ab','ac','ad','bc','bd'....) 
    for i in range(0,len(all_substrings)):
        if(len(all_substrings) ==k):
            all_substrings.pop()# only print substrings equal to k and generate list of substrings
    newlst=[]
    for item in all_substrings:
        if len(item) ==k:
            newlst.append(item)
    unique_set=set(newlst)
    unique_list=list([unique_set])#only get unique substrings equal to k and ignore repeats
    for x in unique_list:
        return (len(x))#prints number of observed substrings for specified k value
poslist=[]
obslist=[]
kvalues=[]
def create_df(mylist):#function to get the data frame for all k values, number of all possible substrings, and number of all observed substrings for a specific list
    for k in range(1,len(mylist)+1):
        '''input is a string of letters
        returns data table of number of unique observed substrings and number of possible substrings for each value of k'''
        obskmers=(observed_substrings(mylist,k))
        obslist.append(obskmers)
    for k in range(1,len(mylist)+1):
        poskmers=(sub_str_possible(mylist,k))
        poslist.append(poskmers)
    for k in range(1,len(mylist)+1):
        kvalues.append(k)
    data={'k': kvalues,
        'observed kmers':obslist,
        'possible kmers':poslist}
    df=pd.DataFrame(data)
    return (df)
print(mylist)#curent list being analyzed
print(create_df(mylist))
print((sum(obslist))/(sum(poslist)))#linguistic complexity

#########################################################################
mylist='ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT'
poslist=[]
obslist=[]
kvalues=[]
def create_df(mylist):#function to get the data frame 3 columns 9 rows, k<10 to match assignment
    for k in range(1,len(mylist)+1):
        obskmers=(observed_substrings(mylist,k))
        obslist.append(obskmers)
    for k in range(1,len(mylist)+1):
        poskmers=(sub_str_possible(mylist,k))
        poslist.append(poskmers)
    for k in range(1,len(mylist)+1):
        kvalues.append(k)
    data={'k': kvalues,
        'observed kmers':obslist,
        'possible kmers':poslist}
    df=pd.DataFrame(data)
    return (df)
print(mylist)#curent list being analyzed
print(create_df(mylist))
print((sum(obslist))/(sum(poslist)))#linguistic complexity
###################################################################################
mylist='ATATATATATATATATA'
poslist=[]
obslist=[]
kvalues=[]
def create_df(mylist):#function to get the data frame 3 columns 9 rows, k<10 to match assignment
    for k in range(1,len(mylist)+1):
        obskmers=(observed_substrings(mylist,k))
        obslist.append(obskmers)
    for k in range(1,len(mylist)+1):
        poskmers=(sub_str_possible(mylist,k))
        poslist.append(poskmers)
    for k in range(1,len(mylist)+1):
        kvalues.append(k)
    data={'k': kvalues,
        'observed kmers':obslist,
        'possible kmers':poslist}
    df=pd.DataFrame(data)
    return (df)
print(mylist)#curent list being analyzed
print(create_df(mylist))
print((sum(obslist))/(sum(poslist)))#linguistic complexity
