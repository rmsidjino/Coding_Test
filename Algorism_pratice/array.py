import numpy as np

arr=[4,1,3,2]

def solution(arr):
    arr = np.array(arr)
    lst = np.array([i for i in range(1,len(arr)+1)])
    if arr.var() == lst.var():
        return True
    else:
        return False

def merge(left, right):
    sorted = []
    # 임시 배열에 작은 순서대로 정렬하여 삽입하기
    i = 0
    j = 0
    # print(left, right)
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    # 남은 원소 삽입하기
    ## 왼쪽 리스트가 모두 삽입되어, 오른쪽 리스트를 모두 삽입하지 못한 경우
    if i == len(left):
        for t in range(j, len(right)):
            sorted.append(right[t])
    ## 오른쪽 리스트가 모두 삽입되어, 왼쪽 리스트를 모두 삽입하지 못한 경우
    if j == len(right):
        for t in range(i, len(left)):
            sorted.append(left[t])

    return sorted

def mergesort(arr):
    # 배열의 크기가 0 또는 1일 경우, 정렬할 필요 없으므로 그대로 return
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])  # 분할 (왼쪽 부분)
    right = mergesort(arr[mid:])  # 분할 (오른쪽 부분)
    return merge(left, right)  # 정복 및 결합

def solution(arr):
    merge_list = mergesort(arr)
    print(merge_list)
    j = 1
    for i in range(0,len(merge_list)):
        print(merge_list[i],j,i)
        if merge_list[i] != j:
            return False
        else:
            j += 1
            print(len(merge_list))
            if i == len(merge_list)-1:
                return True
def solution(arr):
    arr = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != i+1:
            return False
    return True
