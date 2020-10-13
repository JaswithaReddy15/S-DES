#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:46:15 2020

@author: jaswithareddy
"""

def funcIP(ip,key):
    IP=[]
    for i in ip:
        IP.append(key[i-1])
    return IP


def leftdiv(IP):
    L=[]
    for i in range(0,4):
        L.append(IP[i])
    return L

def rightdiv(IP):
    R=[]
    for i in range(4,8):
        R.append(IP[i])
    return R


def funcEP(ep,R):
    EP=[]
    for i in ep:
        EP.append(R[i-1])
    return EP


def funcXOR8(EP,k1):
    xor=[]
    for i in range(8):
        if EP[i]==k1[i]:
            xor.append('0')
        else:
            xor.append('1')
    return xor


def SBox(s0,s1,S0,S1):
    temp=[]
    #eg: ['1','0','1','0']=>['10','01']=>[2,1] where 2 is used to find row in S-Box and 1 is used to find column in S-Box
    t1=[int(S0[0]+S0[3],2),int(S0[1]+S0[2],2)] 
    t2=[int(S1[0]+S1[3],2),int(S1[1]+S1[2],2)]
    #searches the S-Box row and column and converts them to binary like '0b01' or '0b0'
    temp.append(bin(s0[t1[0]][t1[1]]))
    temp.append(bin(s1[t2[0]][t2[1]]))
    for i in range(2):
        if temp[i]=='0b0':
            temp[i]='00'
        else:
            temp[i]=temp[i][2:]
    #eg: to convert ['01','00'] stored in temp to ['0','1','0,'0'] which will be stored in S
    a,b=[i[0] for i in temp]
    c,d=[i[1] for i in temp]
    S=[a,c,b,d]
    return S    


def funcP4(p4,S):
    P4=[]
    for i in p4:
        P4.append(S[i-1])
    return P4    


def funcXOR4(P4,L):
    xorL=[]
    for i in range(4):
        if P4[i]==L[i]:
            xorL.append('0')
        else:
            xorL.append('1')
    return xorL


if __name__=='__main__':
    flag=1 #to check for validity of input
    inpkey=[]
    k=input(("Enter a 8 bit key in binary: "))
    # converting input string into list
    for i in k:
        if i=='0' or i=='1':
            inpkey.append(i) # turning input into list
        else:
            flag=0
            break
    if len(inpkey)!=8: # to check length of input
        flag=0
    
    if flag==1:
        # all the lists below are already given 
        ip=[2,6,3,1,4,8,5,7]
        ip_1=[4,1,3,5,7,2,8,6]
        ep=[4,1,2,3,2,3,4,1]
        p4=[2,4,3,1]
        s0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
        s1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
        
        # calling function to perform initial permutation (IP)
        IP=funcIP(ip,inpkey)
        print("After applying IP: ",IP)
        
        #calling function to divide IP into L and R
        L=leftdiv(IP)
        R=rightdiv(IP)
        print("Dividing IP into L = ",L,"and R = ",R)
        
        #calling function to apply EP to R
        EP=funcEP(ep,R)
        print("After applying EP to R: ",EP)
        
        #input key1
        k1flag=1 # to check validity of key1
        k1=[]
        x=input("Enter Key1: ")
        for i in x:
            if i=='0' or i=='1':
                k1.append(i)
            else:
                k1flag=0
                break
        if len(k1)!=8: # to check length of Key1
            k1flag=0
        
        if k1flag==1:
            print("Key1: ",k1)
            
            #calling function to xor EP with K1
            xor=funcXOR8(EP,k1)
            print("XOR EP with Key1: ",xor)
            
            #calling function to divide xor into S0 and S1
            S0=leftdiv(xor)
            S1=rightdiv(xor)
            print("Dividing XOR into S0 = ",S0,"and S1 = ",S1)
            
            #finding result from S0 and S1
            outputS=SBox(s0,s1,S0,S1)
            print("After applying S-Box rules: ",outputS)
            
            #calling function to perform P4
            P4=funcP4(p4,outputS)
            print("After applying P4: ",P4)
            
            #calling function to xor P4 with L
            xorL=funcXOR4(P4,L)
            print("XOR of P4 with L: ",xorL)
            
            #------------------------------------------------------------------
            #------------------------------------------------------------------
        
            #swap xorL with R
            xorL,R=R,xorL
            print("After swapping: XOR of P4 with L = ",xorL," and R = ",R)
        
            #calling function to apply EP to R
            EP_1=funcEP(ep,R)
            print("After applying EP to R: ",EP_1)
            
            #input key2
            k2flag=1 # to check validity of key2
            k2=[]
            x=input("Enter Key2: ")
            for i in x:
                if i=='0' or i=='1':
                    k2.append(i)
                else:
                    k2flag=0
                    break
            if len(k2)!=8: # to check length of Key2
                k2flag=0
            
            if k2flag==1:
                print("Key2: ",k2)
                
                #calling function to xor EP with K2
                xor1=funcXOR8(EP_1,k2)
                print("XOR EP with Key2: ",xor1)
                
                #calling function to divide xor into S0 and S1
                S0_1=leftdiv(xor1)
                S1_1=rightdiv(xor1)
                print("Dividing XOR into S0 = ",S0_1,"and S1 = ",S1_1)
                
                #finding result from S0 and S1
                outputS_1=SBox(s0,s1,S0_1,S1_1)
                print("After applying S-Box rules: ",outputS_1)
                
                #calling function to perform P4
                P4_1=funcP4(p4,outputS_1)
                print("After applying P4: ",P4_1)
                
                #calling function to xor P4 with L
                xorL_1=funcXOR4(P4_1,xorL)
                print("XOR of P4 with L after swapping: ",xorL_1)
                
                #combining xorL_1 with R after swapping
                finalTemp=xorL_1+R
                
                #calling function to perfrom intital permutation inverse
                IP_1=funcIP(ip_1,finalTemp)
                print("After applying IP: ",IP_1)
                
                print()
                
                print("Encryption: ",end='')
                for i in range(len(IP_1)):
                    print(IP_1[i],end='')
                
            else:
                print("Invalid Key-2")
        else:
            print("Invalid Key-1")   
    else:
        print("Invalid Key")
