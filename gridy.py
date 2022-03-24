# Gridy 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# ex3-1(p87) O(K)
n = 1260
cnt = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    cnt += n # cnt = 1260 / cnt = 1260+260=1520 / cnt = 1520+60=1580 / cnt = 1580+10=1590
    n %= coin # n=260 / n=60 / n=10 / n=0
print(cnt)

# ex3-2(p92)
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
n = 5
m = 8
k = 3
data = [2,4,5,4,6]
data.sort()
print(n,m,k,data)
first = data[n - 1]
second = data[n - 2]
res = 0

while True:
    for i in range(k):
        if m == 0:
            break
        res += first
        m -= 1
    if m == 0:
        break
    res += second
    m -= 1

print(res)

#ex3-3 (30min)
n, m = map(int, input().split())
arr_data = []
res = []
for i in range(0,n):
    data = list(map(int, input().split()))
    arr_data.append(data)
    res.append(min(arr_data[i]))
# print(arr_data)
print(max(res))
#--------------------
# test = [[7,3,1,8],
#         [3,3,3,4],]
#
# res = []
# res.append(min(test[0]))
# res.append(min(test[1]))
# res.append(min(test[2]))
# print(res, max(res))
#--------------------
#ex3-3 answer
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = (min(data))
    result = max(result, min_value)
print(result)

#ex3-4 answer
n, k = map(int, input().split())
res = 0

while n >= k:
    while n % k != 0:
        n -= 1
        res += 1
    n //= k
    res += 1
while n>1:
    n -= 1
    res += 1
print(res)
