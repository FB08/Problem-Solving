# pen2402님 Sliding Window 기법 참고
def solution():
    import os
    input = map(int, os.read(0, os.fstat(0).st_size).split())
    N, M = next(input), next(input)
    prefix_sum = [0]*(N+1)
    for i in range(1, N+1):
        prefix_sum[i] = prefix_sum[i-1]+next(input)
    res = min_val = 0
    for i in range(M, N+1):
        if prefix_sum[i-M] < min_val: # i-M개 이하의 prefix_sum값중 가장 작은 값을 빼야 최댓값
            min_val = prefix_sum[i-M]
        if prefix_sum[i]-min_val > res: # 최댓값 갱신
            res = prefix_sum[i]-min_val
    os.write(1, str(res).encode())
    os._exit(0)
solution()
#==========[ Sliding Window ]==========
# - 길이가 고정된 윈도우(부분 배열)이 이동하며 데이터를 탐색
# - 투포인터는 길이가 가변적이라는 점에서 상이
# - 네트워크 패킷 송신과 관련하여 많이 사용됨됨
# - 이 문제에서의 이용:
# - 길이가 M이상이 되어야하므로 prefix_sum[i]에서 i-M보다 작은 값의 prefix_sum중 가장 작은 값을 빼면 된다는 점을 이용

# 참고:
# 지역변수는 LOAD_FAST 연산, 전역변수는 LOAD_GLOBAL 연산 이용하여 지역변수 연산이 더 빠름름
# -> 함수로 정의하여 호출하면 전역(Global) 변수가 아니라 지역(Local) 변수를 이용하므로 함수 호출이 빠름
# Python Garbage Collector는 지역 변수에서 메모리를 더 빨리 회수하므로 이점이 있음
# => def solution(): [code]  solution()을 이용하는게 코드가 더 빠르다
