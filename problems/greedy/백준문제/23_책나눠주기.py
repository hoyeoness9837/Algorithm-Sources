# 백준이는 방 청소를 하면서 필요 없는 전공 서적을 사람들에게 나눠주려고 한다. 나눠줄 책을 모아보니 총 N권이었다. 책이 너무 많기 때문에 백준이는 책을 구분하기 위해 각각 1부터 N까지의 정수 번호를 중복되지 않게 매겨 두었다.
# 조사를 해 보니 책을 원하는 서강대학교 학부생이 총 M명이었다. 백준이는 이 M명에게 신청서에 두 정수 a, b (1 ≤ a ≤ b ≤ N)를 적어 내라고 했다. 그러면 백준이는 책 번호가 a 이상 b 이하인 책 중 남아있는 책 한 권을 골라 그 학생에게 준다. 만약 a번부터 b번까지의 모든 책을 이미 다른 학생에게 주고 없다면 그 학생에게는 책을 주지 않는다.
# 백준이가 책을 줄 수 있는 최대 학생 수를 구하시오.
# 첫째 줄에 테스트 케이스의 수가 주어진다.
# 각 케이스의 첫 줄에 정수 N과 M이 주어진다. 다음 줄부터 M개의 줄에는 각각 정수 ai, bi가 주어진다. (1 ≤ ai ≤ bi ≤ N)
#my answer
test = int(input())
data = []
count = 0
for i in range(test):
  N, M = map(int, input().split())
  for j in range(M):
    a, b = map(int, input().split())
    data.append([a,b])

    if data[j] != data[j+1]:
      count += b - a

  while count < N:
    print(count)
  else:
    print(N)
  
#answer 
#끝나는 번호 가 더 큰지에 대해서 는 알 수가 없다.  예를 들어  앞에 있는 친구가 가져갈 수 있는 책의 번호가
# 3 ~9라고 해보자 뒤에 있는 친구는 3 ~ 3이다 (a 이상 b 이하 )       N이 4이고 다음에 주어야 할 책의 번호가 3이라 하면  앞에서 3번이라는 책을 주게 되면 그다음 친구는  책을 받을 수 없다. 앞에 있는 친구가 4번 책을 가져가면 다음에 있는 친구가 3번 책을 가져갈 수 있는데도 말이다. 이러한 상황으로 인해서 우선적으로 정렬은 책의 끝 번호(b)가 작은 번호들이 앞으로 올 수 있도록 정렬. 근시적으로 작은 책들의 번호가 앞 배열로 정렬되게 된다. 이때 만약 책 끝번호가 같을 때 책의 시작 번호 중 작은 값들이 앞으로 오도록 정렬해주면 앞에 일어난 상황이 일어나지 않게 된다. 정렬을 한뒤 a 부터 b 까지 방문하지 않은 book을 체크하고, 카운터를 증가.
trial = int(input())

for _ in range(trial):
  n, m = map(int, input().split())
  
  books = [False] * (n+1) # 방문하지 않음으로 초기화

  requests = [] #어떤 책을 받고싶은지 리퀘스트 받아줌
  for _ in range(m):
    requests.append(list(map(int, input().split())))
  requests.sort(key = lambda x : x[1]) # a,b 중에서 b(x[1])을 오름차순으로 정렬

  count = 0 
  while requests: # 리퀘스트가 다 소비될때까지
    a, b = requests.pop(0) # 끝번호가 작은순서대로 정렬된 상태의 리퀘스트중 맨 앞부분을 뽑아 

    for i in range(a, b+1): # a이상 b 이하의 범위내에 
      if not books[i]: # 만약 책이 방문되지 않았다면 (누가 가져가지 않았다면)
        count += 1 # 가져갈수있고
        books[i] = True # 방문되었다(가져갔다)로 처리
        break # 모두 방문된부분일경우에는 탈출.
  
  print(count)