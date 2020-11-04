import sys
import random
import time
# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements 
        R = arr[mid:] # into 2 halves
 
        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half
 
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
    seeds = [1,2,3]
    n_ns = [1000, 1500, 2000, 2500, 3000, 5000]
    
    for n_n in n_ns:
        for seed in seeds:
            print("current number of elements is {}, current seed is {}".format(n_n, seed))

            arr0,arr1 = [],[]
            for i in range(n_n):
                 tempRandNum = random.randint(0,sys.maxsize)
                 arr0.append(tempRandNum)
                 arr1.append(tempRandNum)
    

            start_m = time.time()
            mergeSort(arr0)
            end_m = time.time()
            total_m = end_m - start_m
            print("{:<20s} {}".format("mergeSort:", total_m))

            start_i = time.time()
            insertionSort(arr1)
            end_i = time.time()
            total_i = end_i - start_i
            print("{:<20s} {}".format("insertionSort:", total_i))


 
# This code is contributed by Mayank Khanna
# https://www.geeksforgeeks.org/merge-sort/
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/