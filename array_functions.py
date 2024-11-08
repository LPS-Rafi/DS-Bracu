import numpy as np

def resize_array(array, new_size):
    arr2 = np.array([0]*new_size)
    for i in range(len(array)):
        arr2[i] = array[i]
    return arr2


def copy_array(array):
    arr2 = np.array([0]*len(array))
    for i in range(len(array)):
        arr2[i] = array[i]
    return arr2

# [5,2,8,11,1]

def shif_left(arr):
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=0
    return arr

#[2,8,11,1,0]


def rotate_left(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1] = temp
    return arr

#[8,11,1,0,2]

def rotate_right(arr):
    temp = arr[len(arr)-1]
    for i in range(len(arr)-1,0):
        arr[i]=arr[i-1]
    arr[0]=temp

#[2,8,11,1,0]

def reverse_out_place(arr):
    arr2 = np.array([0]*len(arr))
    i = 0 
    while (i<len(arr)-1):
        arr2[i]=arr[len(arr)-1-i]
        i+=1
    return arr2

#[0,1,11,8,2]

def reverse(arr):
    j=len(arr)-1
    for i in range(len(arr)//2):
        arr[i],arr[j]=arr[j],arr[i]
        j-=1
    return arr

def insert_end(arr,size,key):
    if size==len(arr):
        arr = resize_array(arr,size+1)
    arr[size]=key
    return arr

def insert_anywhere(arr,size,index,key):
    if index<0 or index>=size:
        return "error"
    if size == len(arr):
        arr = resize_array(arr,size+1)
    for i in range(size,index,-1):
        arr[i]=arr[i-1]
    arr[index]=key
    return arr

def delete_end(arr,size):
    if size == 0:
        return "Error"
    arr[size-1]=0
    return arr

def delete_anywhere(arr,size,index):
    if size == 0 or (index<0 and index<=size):
        return "Error"
    for i in range(index, size-1):
        arr[i]= arr[i+1]
    arr[size-1]=0
    return arr

#2D
def array_sum(arr):
    sum = 0
    row, col = arr.shape
    for i in range(row):
        for j in range(col):
            sum+=arr[i][j]
    return sum

def row_wise_sum(arr):
    row,col = arr.shape
    result = np.array(([0]*row,[0]*1))
    for i in range(row):
        for j in range(col):
            result[i][0]+=arr[i][j]
    return result

def col_wise_sum(arr):
    row,col = arr.shape
    result = np.zerors((1,col),dtype=int)
    for i in range(col):
        for j in range(row):
            result[0][i]+=arr[j][i]
    return result