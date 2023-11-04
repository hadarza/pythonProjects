def allSumsDP(arr):
    
    sums = set()
    values_calculated = {}

    def arr_sum(index, value):

        if (index, value) in values_calculated: return values_calculated[(index, value)]
        if index == len(arr): return {value}

        res = arr_sum(index + 1, value + arr[index]) | arr_sum(index + 1, value)
        values_calculated[(index, value)] = res

        return res

    sums = arr_sum(0, 0)
    return sums