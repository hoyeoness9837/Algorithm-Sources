https://www.acmicpc.net/problem/2812
N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
N, K = map(int, input().split())
number = list(map(int, list(input())))
number.sort(reverse = True)
result = []
for i in range(0, N-K):
  result.append(number[i])
print(*result, sep = '')

##asnwer
n, k = map(int, input().split())
number = list(input().strip())
result = []
for i in range(n):
  while k > 0 and result and result[-1] < number[i]: # 남은 k가 있고, 결과가 있고, 결과의맨뒷자리 숫자보다 큰 숫자인경우만
    del result[-1] #가장작은 맨뒷자리수를 지워주고
    k -= 1 #지운만큼 k를 깎아준다.
  result.append(number[i]) # 그 숫자들로 채워준다.
print(''.join(result[:n - k])) # 모든 숫자를 콤마를 제외한 숫자의 일렬로만 프린트한다.