파이썬 Multiprocessing 



파이썬은 기본적으로 싱글쓰레드에서 순차적으로 작동한다. 따라서 병렬처리를 위해서는 따로 module을 불러 구현한다.

1. argparse를 사용하여 number과 사용할 process수를 받는다
2. csv파일로 찾은 prime number들과 time을 기록한다



```python
def isprime(n):
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if not n%i:
            return False
    return True

def return_prime(start,end,prime_list):
    for i in range(start,end+1):
        if isprime(i):
            prime_list.append(i)
```

위는 single process와 multi process의 공통코드들이다
결과를 확인해보면 확실히 매우 빠르다...
추후에 pool, multi thread, queue 도 같은 코드로 추가 예정...



