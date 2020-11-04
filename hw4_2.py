import sys
import random
import time
# Python program for implementation of MergeSort
def mergeSort(arr, k):
    if len(arr) >1:
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements 
        R = arr[mid:] # into 2 halves

        # Sorting the first half
        if len(L) < k:
            insertionSort(L)
        else:
            mergeSort(L,k) 

        # Sorting the second half
        if len(R) < k:
            insertionSort(R)
        else:
            mergeSort(R,k) 
 
        i = j = k = 0
         
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1
         
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1
         
        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1
 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
 
# driver code to test the above code
if __name__ == '__main__':
    seeds = [1,2,3,4,5]
    n_n = 10000
    ks = [0,10,15,20,25,30,40,100,150]

    for k in ks:
        ma = 0
        ia = 0
        for seed in seeds:
            
            arr0 = []
            for i in range(n_n):
                 tempRandNum = random.randint(0,sys.maxsize)
                 arr0.append(tempRandNum)  

            start_m = time.time()
            mergeSort(arr0, k)
            end_m = time.time()
            total_m = end_m - start_m
            ma += total_m


        ma /= 5

        print("current value of k is {}".format(k))
        print("{:<20s} {}".format("mergeSort:", ma))

        
    print("end")
 
# This code is contributed by Mayank Khanna
# https://www.geeksforgeeks.org/merge-sort/
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/