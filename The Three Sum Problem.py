def threeSumSolution(arr, n, target):
    # arr is without any duplicates
    arr.sort()
    result = []
    for i in range(n-2):
        left = i+1
        right = n-1
        while left < right:
            curr = (arr[i] + arr[left] + arr[right])
            if curr == target:
                result.append([arr[i], arr[left], arr[right]])
                left +=1
                right -= 1
            elif curr < target:
                left += 1
            else:
                right -= 1
    if len(result) == 0:
        return ["No Pairs found"]
    else:
        return result


num = int(input())
instr = list(map(int,input().split(",")))
targetSum = int(input())
ans = threeSumSolution(instr, num, targetSum)
print(ans)