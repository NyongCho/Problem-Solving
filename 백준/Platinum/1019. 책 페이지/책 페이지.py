import sys
input = sys.stdin.readline

def count_0(count):
    x = 0

    tmp = 0
    for i in range(count-1):
        tmp += 9*(10**i)
        x += tmp

    return x

def pattern(num, count):
    x = 11 + (count-3)*(10**(count-2)) + (count-3)
    tmp = 10
    for _ in range(count-3):
        x += tmp * 8
        tmp *= 10
    y = (count-1)*(10**(count-2))
    z = (10**(count-1)) + (count-2)*(10**(count-2))
    tmp = 1
    for _ in range(count-2):
        z += tmp*9
        tmp *= 10

    result = [y for _ in range(10)]
    if num == 1:
        result[0] = x
    else:
        result[num-1] = z

    result[num] += 1

    return result

def digit_count(origin, n, count):
    num = n//(10**(count-1))

    # 숫자가 100 이하일 경우 그냥 세기
    if n <= 100 or (count <= 3 and num == 1):
        count = [0] * 10
        for i in range(1, n+1):
            m = i
            while m > 0:
                count[m % 10] += 1
                m //= 10
        return count

    # 아닐 경우
    result = [0 for _ in range(10)]

    if num == 0:
        return digit_count(origin, n, count-1)

    # 패턴대로 가장 큰 자리수까지 count 구하기
    for i in range(1, num+1):
        output = pattern(i, count)
        for j in range(10):
            result[j] += output[j]

    # 나머지 숫자만큼 바로 윗 자리수 더해주기
    front = origin//(10**(count-1))
    rear = origin%(10**(count-1))

    pre = [0 for _ in range(10)]
    pre[front%10] += rear

    # 중간에 0 세어주기 
    for i in range(count-1):
        m = (origin // (10**(count-2-i)))%10
        if m != 0:
            pre[0] += count_0(count-1-i)
            break
        else:
            pre[0] += rear
    
    remain = digit_count(origin, rear, count-1)

    for i in range(10):
        result[i] += pre[i] + remain[i]

    return result

n = int(input())

count = 0
m = n

while m > 0:
    count += 1
    m //= 10

ans = digit_count(n, n, count)
print(*ans)