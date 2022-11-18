def pivot_sort(arr, min_Value = 0, max_Value = 2**64):
    # Set up pivot and array
    avg = sum(arr)/len(arr)
    new_arr = [max_Value] * (len(arr) + 1)
    i = 0
    x = 0
    # Create new_arr values
    while i < len(arr):
        if avg > arr[i]:
            x += 1
        i += 1
    new_arr[x] = avg
    i = 0
    while i < x:
        new_arr[i] = min_Value
        i += 1
    minus = x
    plus = x
    i = 0
    # Loop through the array
    while i < len(arr):
        n = x
        if arr[i] < avg: # Check if current value is lower than the pivot
            n -= 1
            minus -= 1
            while n >= minus:
                if arr[i] > new_arr[n]: # Check if current value is higher than the set value in new_arr
                    # If true push all values in new_arr
                    temp = new_arr[n]
                    new_arr[n] = arr[i]
                    while n > minus:
                        n -= 1
                        temp2 = new_arr[n]
                        new_arr[n] = temp
                        temp = temp2
                n -= 1
        else:
            n += 1
            plus += 1 
            while n <= plus:
                if arr[i] < new_arr[n]: # Check if current value is lower than the set value in new_arr
                    # If true push all values in new_arr
                    temp = new_arr[n]
                    new_arr[n] = arr[i]
                    while n < plus:
                        n += 1
                        temp2 = new_arr[n]
                        new_arr[n] = temp
                        temp = temp2
                n += 1
        i += 1
    new_arr.pop(x)
    return new_arr
