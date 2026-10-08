#counting subarrays containing at least one even number


a = [1,3,2,5,7,6]

l = 0 
c = 0 
even = 0 
n = len(a)

for r in range(n):
    if a[r]%2 == 0:
        even+=1 
    while even:
        c += (n-r)  #extensions of [l---r] through end
        if a[l]%2 == 0:
            even -= 1
        l += 1

print(c)


# 1423. Maximum Points You Can Obtain from Cards
# 1004. Max Consecutive Ones III
# 1358. Number of Substrings Containing All Three Characters.  atleast k type 

# 930. Binary Subarrays With Sum atmost k type


# 560. Subarray Sum Equals K,,,, works with negative numbers as well sliding window does not work with negative numbers