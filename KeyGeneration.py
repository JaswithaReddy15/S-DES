#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:18:20 2020

@author: jaswithareddy
"""

def permutation10(p10,key):
    key10=[]
    for i in p10:
        key10.append(key[i-1])
    return key10

        
def ls(key,n):
    # n=1: performs circular left shift once
    # n=2: performs circular left shift twice
    # applying circular left shift to first half
    for j in range(n):
        temp1=key[0]
        for i in range(4):
            key[i]=key[i+1]
        key[4]=temp1
    # applying circular left shift to second half
    for j in range(n):
        temp2=key[5]
        for i in range(5,9):
            key[i]=key[i+1]
        key[9]=temp2
    return key


def permutation8(p8,key):
    key8=[]
    for i in p8:
        key8.append(key[i-1])
    return key8
    

if __name__=='__main__':
    p10=[3,5,2,7,4,10,1,9,8,6] # P10 already given
    p8=[6,3,7,4,8,5,10,9] # P8 already given
    
    inpkey=[] # initializing key list
    k=input(("Enter a 10 bit key in binary: "))# taking key as a string input
    for i in k:
        inpkey.append(i) # turning string into list
        
    #calling function to perform P10
    key10=permutation10(p10,inpkey) 
    print("After permuating key using P10: ",key10)
    
    #calling function to perform left shift -1
    ls1=ls(key10,1)
    print("After performing left shift-1: ",ls1)
    
    #calling function to perform P8
    key1=permutation8(p8,ls1)
    print("After permuating key using P8 we get KEY-1: ",key1)
    
    #calling function to perform left shift - 2
    ls2=ls(ls1,2)
    print("After performing left shift-2: ",ls2)
    
    #calling function to perform P8
    key2=permutation8(p8,ls2)
    print("After permuating key using P8 we get KEY-2: ",key2)
    
    print("\n")
    
    print("Key1: ",key1)
    print("Key2: ",key2)