import random
import time

def bubblesort(arr):
    """
    implementation of bubble sort
    """
    length = len(arr)
    unsorted = True
    while unsorted and length > 1:
        unsorted = False
        i = 0
        while i < length - 1:
            if arr[i] > arr[i+1]:
                unsorted = True
                arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
    return arr

def selectionsort(arr):
    """
    implementation of selection sort
    """
    length = len(arr)
    for i in range(length - 1):
        min_i = -1
        min = arr[i]
        for j in range(i + 1, length):
            if arr[j] < min:
                min_i = j
                min = arr[j]
        if min_i != -1:
            arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr

def insertionsort(arr):
    """
    implementation of insertion sort
    """
    length = len(arr)
    if length < 2:
        return arr
    for i in range(1, length):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr

def mergesortBU(arr1):
    """
    implementation of bottom-up two-array-swap merge sort
    basicalefty, start by pairing indices 1:1 from the beginning.
    then step up to 2:2, 4:4 until (step > length)
    """
    length = len(arr1)
    if length < 2:
        return arr1
    # make a copy, since mergesort needs O(n) space
    arr2 = arr1[:]
    step = 1
    while step < length:
        i, curr = 0, 0  # beginning of each pair, current write point
        while i + step < length:
            left, right = i, i + step
            limitR = i + 2 * step
            if length < limitR:
                limitR = length
            limitL = i + step
            while left < limitL and right < limitR:
                if arr1[left] <= arr1[right]:
                    arr2[curr] = arr1[left]
                    left += 1
                else:
                    arr2[curr] = arr1[right]
                    right += 1
                curr += 1
            while left < limitL:
                arr2[curr] = arr1[left]
                left += 1
                curr += 1
            while right < limitR:
                arr2[curr] = arr1[right]
                right += 1
                curr += 1
            i += 2 * step
        # important: copy the untouched end to the new array. It's not applied yet
        while curr < length:
            arr2[curr] = arr1[curr]
            curr += 1
        step *= 2
        # swap two arrays for cost efficiency
        arr1, arr2 = arr2, arr1
    return arr1

def mergesortTD(arr):
    length = len(arr)
    if length < 2:
        return arr
    return msortTD(arr[:], arr, 0, len(arr))

def msortTD(arrSrc, arrDst, start, end):
    if end - start <= 1:
        return arrDst
    mid = (start + end) / 2
    msortTD(arrDst, arrSrc, start, mid)
    msortTD(arrDst, arrSrc, mid, end)
    return mergeTD(arrSrc, arrDst, start, end)

def mergeTD(arrSrc, arrDst, start, end):
    mid = (start + end) / 2
    curr = start
    i = start
    j = mid
    while i < mid and j < end:
        if arrSrc[i] <= arrSrc[j]:
            arrDst[curr] = arrSrc[i]
            i += 1
        else:
            arrDst[curr] = arrSrc[j]
            j += 1
        curr += 1
    while i < mid:
        arrDst[curr] = arrSrc[i]
        i += 1
        curr += 1
    while j < end:
        arrDst[curr] = arrSrc[j]
        j += 1
        curr += 1
    return arrDst

def mergesortTDnaive(arr):
    """
    Naive textbook implementation creating many copies of array slices
    """
    return msortTDnaive(arr)

def msortTDnaive(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) / 2
    left = msortTDnaive(arr[:mid])
    right = msortTDnaive(arr[mid:])
    return mergeTDnaive(left, right)

def mergeTDnaive(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def quicksort(arr):
    """
    implementation of quicksort with various options
    """
    #arr = arr[:]
    length = len(arr)
    if length < 2:
        return arr
    random.shuffle(arr)
    qsort(arr, 0, length - 1)
    return arr

def quicksort3(arr):
    """
    implementation of quicksort with various options
    """
    #arr = arr[:]
    length = len(arr)
    if length < 2:
        return arr
    random.shuffle(arr)
    qsort3p(arr, 0, length - 1)
    return arr

def make_median_pivot(arr, start, end):
    if arr[start] > arr[end]:
        if arr[end] >= arr[(start+end)/2]:
            arr[start], arr[end] = arr[end], arr[start]
        elif arr[start] > arr[(start+end)/2]:
            arr[start], arr[(start+end)/2] = arr[(start+end)/2], arr[start]
    elif arr[start] < arr[end]:
        if arr[end] <= arr[(start+end)/2]:
            arr[start], arr[end] = arr[end], arr[start]
        elif arr[start] < arr[(start+end)/2]:
            arr[start], arr[(start+end)/2] = arr[(start+end)/2], arr[start]

def qsort(arr, start, end):
    """
    Regular two-partition quicksort
    Jon Bentley's two-sided partition scheme
    [p| ---- <= p ---- | ---- ? ---- | ---- >= p ---- ]
    eliminates O(n2) worst case on uniform array.
    """
    if end <= start:
        return
    p = arr[start]
    i = start
    j = end + 1
    while True:
        i += 1
        j -= 1
        while i <= j and arr[i] < p:
            i += 1
        while arr[j] > p:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[start], arr[i-1] = arr[i-1], arr[start]
    qsort(arr, start, i - 2)
    qsort(arr, i, end)

def qsort3p(arr, start, end):
    """
    Three-partition quicksort based on Bentley's algorithm
    This algorithm uses four pointers to push equal partitions
    to the both side and then swap them to center.
    """
    if end <= start:
        return
    p = arr[start]  # pivot = leftmost element
    left = start      # edge of the left 
    right = end        # edge
    i = start + 1   # current left item
    j = end         # current right item
    # variables for equal partition count on left and right
    left = 0
    right = 0

    while True:
        # terminate when i crosses r
        while i <= end and arr[i] < p:
            i += 1
        while i < j and arr[j] > p:
            j -= 1
        if i >= j:
            break

        # if left is not smaleft AND right is not big, swap
        arr[i], arr[j] = arr[j], arr[i]

        # if left item is equal to pivot, swap it to the left
        if arr[i] == p:
            while left < i and arr[left] == p:
                left += 1
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left += 1

        # if right item is equal to pivot, swap it to the right
        if arr[j] == p:
            while right > j and arr[right] == p:
                right -= 1
            arr[j], arr[right] = arr[right], arr[j]
            j -= 1
            right += 1

    # swap the original pivot
    arr[start], arr[i-1] = arr[i-1], arr[start]

    # move aleft same element around pivot
    j = i
    i -= 2
    if arr[right] == p:
        right += 1
    for i in range(left):
        arr[start+1+i], arr[i] = arr[i], arr[start+1+i]
        i -= 1
    for i in range(right):
        arr[end-i], arr[j] = arr[j], arr[end-i]
        j += 1
    qsort3p(arr, start, i)
    qsort3p(arr, j, end)

def issorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def testsort(sort, arrRand, arrSame, arrOrd, arrRev):
    assert([] == sort([]))
    print 'Works on empty array.'
    assert([1] == sort([1]))
    print 'Works on singleton.'
    assert([0,1] == sort([1,0]))
    assert([0,1] == sort([0,1]))
    print 'Works on a trivial case.'
    
    print 'Test 1. Sorting a random array'
    arr = arrRand[:]
    print 'sorting ' + str(len(arr)) + 'numbers'
    t = time.time()
    arr = sort(arr)
    print 'Time elapsed: ' + str(time.time() - t)
    assert(arr == arrOrd)
    print 'Correctly sorted'
    
    print 'Test 2. Sorting a uniform array'
    arr = arrSame[:]
    print 'sorting ' + str(len(arr)) + 'numbers'
    t = time.time()
    arr = sort(arr)
    print 'Time elapsed: ' + str(time.time() - t)
    assert(arr == arrSame)
    print 'Correctly sorted'
    
    print 'Test 3. Sorting a sorted array'
    arr = arrOrd[:]
    print 'sorting ' + str(len(arr)) + 'numbers'
    t = time.time()
    arr = sort(arr)
    print 'Time elapsed: ' + str(time.time() - t)
    assert(arr == arrOrd)
    print 'Correctly sorted'
    
    print 'Test 4. Sorting a reverse-sorted array'
    arr = arrRev[:]
    print 'sorting ' + str(len(arr)) + 'numbers'
    t = time.time()
    arr = sort(arr)
    print 'Time elapsed: ' + str(time.time() - t)
    assert(arr == arrOrd)
    print 'Correctly sorted'

arrRand = [random.randint(0, 1000000) for i in range(1000000 + random.randint(0, 127))]
arrSame = [1 for i in range(10000)]
arrOrd = sorted(arrRand)
arrRev = list(reversed(arrOrd))

print 'bubblesort'
#testsort(bubblesort, arrRand, arrSame, arrOrd, arrRev)
print ''

print 'selectionsort'
#testsort(selectionsort, arrRand, arrSame, arrOrd, arrRev)
print ''

print 'insertionsort'
#testsort(insertionsort, arrRand, arrSame, arrOrd, arrRev)
print ''

print 'mergesort bottom-up'
testsort(mergesortBU, arrRand, arrSame, arrOrd, arrRev)
print ''

print 'mergesort top-down'
testsort(mergesortTD, arrRand, arrSame, arrOrd, arrRev)
print ''

print 'mergesort top-down naive'
testsort(mergesortTDnaive, arrRand, arrSame, arrOrd, arrRev)
print ''

print 'quicksort regular.'
testsort(quicksort, arrRand, arrSame, arrOrd, arrRev)
print ''

print 'quicksort three-part'
#testsort(quicksort3, arrRand, arrSame, arrOrd, arrRev)
print ''

