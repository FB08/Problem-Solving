# kiwiyou님 카데인 알고리즘 참고
def main():
    import os
    nums = map(int, os.read(0, os.fstat(0).st_size).split()) # os.read()로 빠른 입력
    s = -(1 << 29) # 최대값을 매우 작은수(=-2^29)로 설정정
    c = -(1 << 29)
    next(nums)
    for x in nums:
        c = (c if c > 0 else 0) + x # x까지의 연속합이 음수라면 기존합+x<x이므로 기존합에 0저장
        s = s if s > c else c # 최댓값 갱신
    os.write(1, str(s).encode()) # encode(인코딩 방식, 기본=UTP-8): str -> byte
    os._exit(0) # 프로그램 즉시 종료

main()

#==========[ Kadane's Algorithm ]==========
# - 배열의 최대 부분합을 구하는 알고리즘
# - 시간복잡도: O(n), 공간복잡도: O(1)
# - 시간복잡도는 DP와 같지만 공간복잡도의 효율이 훨씬 좋다
# - 또한 max()알고리즘을 사용하지 않아도 되므로 연속합 문제에 특화됨

#==========[ 문법 ]==========
# os.read(fd, size):
# 파일 디스크립터 fd에서 size바이트를 읽는다
# fd=0은 표준 입력, fd=1은 표준 출력, fd=2는 표준 오류

# os.fstat(fd):
# 파일 디스크립터 fd의 상태 정보를 반환
# .st_size는 파일의 총 크기(바이트)를 반환환

# os.write(fd, data):
# 파일 디스크립터 fd에 바이트(byte) 형식으로 출력할 data
# - print(str)와 차이점:
#       print: Python 내부 I/O 버퍼 사용 |  os.write: 시스템 호출(syscall) 직접 수행
#       print: str형식 사용              |  os.write: byte형식 사용
#       print: 자동 개행(\n)             |  os.write: 개행 x

# os._exit(code):
# 불필요한 후처리 없이 즉시 모든 스레드의 프로세스를 종료함
# code=0은 정상 종료, code=-1은 오류, 나머지는 비정상 종료를 뜻함
# 파일 닫기나 버퍼 플러시시를 하지 않으므로 데이터 손실 가능성 있음
# - sys.exit()과 차이점:
#       SystemExit 예외 발생(try-except O)
#       finally 블록 실행
#       파일 닫기, 버퍼 플러시 자동 처리
#       서브 스레드 종료 x