import random
import time

def bubblesort(arr, option):
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

def selectionsort(arr, option):
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

def insertionsort(arr, option):
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

def mergesortBU(arr1, option):
    """
    implementation of bottom-up two-array-swap merge sort
    basically, start by pairing indices 1:1 from the beginning.
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
            while curr < length and curr < i + 2 * step:
                if right == length or right == i + 2 * step:
                    arr2[curr] = arr1[left]
                    left += 1
                elif left == i + step:
                    arr2[curr] = arr1[right]
                    right += 1
                elif arr1[left] <= arr1[right]:
                    arr2[curr] = arr1[left]
                    left += 1
                elif arr1[left] > arr1[right]:
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

def quicksort(arr, option):
    """
    implementation of quicksort with various options
    '': quicksort with leftmost element as pivot
    's': shuffle before sort
    '3': three-part quicksort
    'i': finish with insertion sort
    """
    #arr = arr[:]
    length = len(arr)
    if length < 2:
        return arr
    if 's' in option:
        random.shuffle(arr)
    if '3' in option:
        qsort3p(arr, 0, length - 1, option)
    else:
        qsort(arr, 0, length - 1, option)
    if 'i' in option:
        return insertionsort(arr, '')
    else:
        return arr

def qsort(arr, start, end, option):
    """
    Regular two-partition quicksort
    """
    if end <= start or ('i' in option and end - start <= 12):
        return
    if 'm' in option:
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
    p = arr[start]
    i = start + 1
    j = end
    while True:
        while i <= j and arr[i] < p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[start], arr[i-1] = arr[i-1], arr[start]
    qsort(arr, start, i - 2, option)
    qsort(arr, i, end, option)

def qsort3p(arr, start, end, option):
    """
    Three-partition quicksort based on Bentley's algorithm
    This algorithm uses four pointers to push equal partitions
    to the both side and then swap them to center.
    """
    if end <= start or ('i' in option and end - start <= 12):
        return
    p = arr[start]  # pivot = leftmost element
    ll = start      # edge of the left 
    rr = end        # edge
    l = start + 1   # current left item
    r = end         # current right item
    # variables for equal partition count on left and right
    left = 0
    right = 0

    while True:
        # terminate when l crosses r
        while l <= end and arr[l] < p:
            l += 1
        while l < r and arr[r] > p:
            r -= 1
        if l >= r:
            break

        # if left is not small AND right is not big, swap
        arr[l], arr[r] = arr[r], arr[l]

        # if left item is equal to pivot, swap it to the left
        if arr[l] == p:
            while ll < l and arr[ll] == p:
                ll += 1
            arr[l], arr[ll] = arr[ll], arr[l]
            l += 1
            left += 1

        # if right item is equal to pivot, swap it to the right
        if arr[r] == p:
            while rr > r and arr[rr] == p:
                rr -= 1
            arr[r], arr[rr] = arr[rr], arr[r]
            r -= 1
            right += 1

    # swap the original pivot
    arr[start], arr[l-1] = arr[l-1], arr[start]

    # move all same element around pivot
    r = l
    l -= 2
    if arr[rr] == p:
        rr += 1
    for i in range(left):
        arr[start+1+i], arr[l] = arr[l], arr[start+1+i]
        l -= 1
    for i in range(right):
        arr[end-i], arr[r] = arr[r], arr[end-i]
        r += 1
    qsort3p(arr, start, l, option)
    qsort3p(arr, r, end, option)

def issorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def testsort(srt, arr1, arr2, arr3, arr4, option):
    print 'Works on empty array: ' + str(not srt([], ''))
    print 'Works on singleton: ' + str([1] == srt([1], ''))
    print 'Works on a trivial case: ' + (str([0,1] == srt([1,0], '')) and str([0,1] == srt([0,1], '')))
    
    print 'Test 1. Sorting a random array'
    arr = arr1[:]
    print 'sorting ' + str(len(arr)) + 'numbers'
    t = time.time()
    arr = srt(arr, option)
    print 'Time elapsed: ' + str(time.time() - t)
    print 'Correctly sorted: ' + str(issorted(arr))
    
    print 'Test 2. Sorting a uniform array'
    arr = arr2[:]
    print 'sorting ' + str(len(arr)) + 'numbers'
    t = time.time()
    arr = srt(arr, option)
    print 'Time elapsed: ' + str(time.time() - t)
    print 'Correctly sorted: ' + str(issorted(arr))
    
    print 'Test 3. Sorting a sorted array'
    arr = arr3[:]
    print 'sorting ' + str(len(arr)) + 'numbers'
    t = time.time()
    arr = srt(arr, option)
    print 'Time elapsed: ' + str(time.time() - t)
    print 'Correctly sorted: ' + str(issorted(arr))
    
    print 'Test 4. Sorting a reverse-sorted array'
    arr = arr4[:]
    print 'sorting ' + str(len(arr)) + 'numbers'
    t = time.time()
    arr = srt(arr, option)
    print 'Time elapsed: ' + str(time.time() - t)
    print 'Correctly sorted: ' + str(issorted(arr))

arrRand = [random.randint(0, 100000) for i in range(1000000 + random.randint(0, 127))]
arrSame = [1 for i in range(1000000)]
arrOrd = sorted(arrRand)
arrRev = list(reversed(arrOrd))

print 'bubblesort'
#testsort(bubblesort, arrRand, arrSame, arrOrd, arrRev, '')
print ''

print 'selectionsort'
#testsort(selectionsort, arrRand, arrSame, arrOrd, arrRev, '')
print ''

print 'insertionsort'
#testsort(insertionsort, arrRand, arrSame, arrOrd, arrRev, '')
print ''

print 'mergesort bottom-up'
#testsort(mergesortBU, arrRand, arrSame, arrOrd, arrRev, '')
print ''

print 'mergesort top-down'
#testsort(mergesortTD, arrRand, arrSame, arrOrd, arrRev, '')
print ''

print 'quicksort regular. Warning: dies on test 2, 3, 4'
#testsort(quicksort, arrRand, arrSame, arrOrd, arrRev, '')
print ''

print 'quicksort shuffle. Warning: dies on test 2'
#testsort(quicksort, arrRand, arrSame, arrOrd, arrRev, 's')
print ''

print 'quicksort median shuffle. Warning: dies on test 2'
#testsort(quicksort, arrRand, arrSame, arrOrd, arrRev, 'sm')
print ''

print 'quicksort shuffle insertion Warning: dies on test 2'
#testsort(quicksort, arrRand, arrSame, arrOrd, arrRev, 'si')
print ''

print 'quicksort three-part'
testsort(quicksort, arrRand, arrSame, arrOrd, arrRev, '3s')
print ''

print 'quicksort three-part insertion'
#testsort(quicksort, arrRand, arrSame, arrOrd, arrRev, '3si')
print ''


