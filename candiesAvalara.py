def candiesMaxSubarraySum(arr, n):
    curr = 0
    maxf = -10**12 - 1

    for i in range(n):
        curr +=arr[i]
        if curr > maxf:
            maxf = curr
        if curr < 0:
            curr = 0
    return maxf

test = int(input())
t = 0
while t < test:
    n = int(input())
    li = list(map(int,input().split()))

    if n > 1:
        x = candiesMaxSubarraySum(li[:-1], n-1)
        y = candiesMaxSubarraySum(li[1:], n-1)

        x = max(x,y)

        if(sum(li)>x):
            print("YES")
        else:
            print("NO")
    else:
        if(li[0]>0):
            print("YES")
        else:
            print("NO")
    t += 1