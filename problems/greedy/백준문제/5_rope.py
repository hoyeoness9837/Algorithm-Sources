# k개의 로프에 무게를 배분해서 한 물체를 들어올릴수 있을때, 최대무게 한계를 구하라.

#내 답 = 시간초과 for loop안에 함수가 너무 많이 있으므로
k = int(input())
data = []
for i in range(k):
    data.append(int(input()))
    data = sorted(data, reverse=True)
    data[i] = data[i] * (i + 1)

result = max(data)
print(result)

#정답: 함수로 정리해, 받아주는 수를 미리 정리후, 
def solution():
    answer = 0
    arr.sort(reverse=True)
    for i in range(N):
        arr[i] = arr[i] * (i + 1) # 가장 쎈 로프 하나 vs 약간로프 여러개, 그중 최대로 버틸수있는 중량찾기. 
    return max(arr)

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input())) 
print(solution())