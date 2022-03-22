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
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
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