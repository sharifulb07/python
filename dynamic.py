

def cutRodRecur(i, price, memo):
    if i==0:
        return 0
    
    if(memo[i-1])!=-1:
        return memo[i-1]
    
    ans=0
    
    for j in range(1, i+1):
        ans=max(ans, price[j-1]+cutRodRecur(i-j,price, memo))
    
    memo[i-1]=ans
    return ans

def cutRod(price):
    n=len(price)
    memo=[-1]*n
    return cutRodRecur(n, price, memo)


arr=[11,22,36,34,58]

result=cutRod(arr)
print(result)


#  //down to top
# def cutRod(price):
#     n=len(price)
#     dp=[0]*(n+1)
#     print(dp)
    
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             dp[i]=max(dp[i], price[j-1]+price[i-j])
#     return dp[n]
    
    





