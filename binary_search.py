arr=[1,2,2,2,3,4,5,10]

def largest_smaller_than_eq(a, t):
    l = 0
    r = len(a) - 1
    ans = -1

    while l <= r:
        md = (l + r) // 2

        if a[md] <= t:
            ans = md       # valid candidate
            l = md + 1     # but try to find a larger index
        else:
            r = md - 1

    return ans

print(largest_smaller_than_eq(arr, 2))


def smallest_greater_than_eq(a,t):
    l = 0 
    r = len(a) - 1
    ans = -1
    while l<=r:
        md = (l+r)//2 
        if a[md] >= t:
            ans = md
            r = md - 1
        else:
            l = md + 1

    return ans 

print(smallest_greater_than_eq(arr,2))
            
