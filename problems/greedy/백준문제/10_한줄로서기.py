#question: 입력 값으로 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있었는지 주어진다. 그리고 줄을 선 순서대로 키를 출력하면 된다. 

출처: https://fullmoon1344.tistory.com/79 [코드이터]
n = int(input())
data = list(map(int, input().split()))

arr = [0] * n #들어갈 정답리스트 초기화
for i in range(1,n+1): #키 1부터 n 까지 
  num_higher = data[i-1] # 입력된 내 왼쪽에 큰사람숫자 받기
  count_zero = 0 # 왼쪽공간
  for j in range(n):
    if count_zero == num_higher and arr[j] == 0: #자신의 왼쪽옆 0수와 자신의 키가 같고, 정답 자리가 비어있다면
      arr[j] = i # 그자리에 삽입
      break
    elif arr[j] == 0: # 자리가 비었지만, 내왼쪽자리0수보다 내 키가 다른경우
      count_zero += 1 # 오른쪽에 남은 자리들을 체크.
print(*arr) # *를 리스트앞에 붙이면 안에 값들만 띄어쓰기로 나눠져서 나온다.

#차례대로 각자 왼쪽에 큰 사람이 몇 명인지를 0의 개수로 판단해서 자리에 넣어준다. 예를 들어 왼쪽에 2명이 있다 하면 결과값 배열에 [0, 0, 현재,...] 자신보다 큰 2명의 자리를, 즉 내 왼쪽의 0을 data[i]만큼 비워두는 자리에 들어간다고 생각하면됨.