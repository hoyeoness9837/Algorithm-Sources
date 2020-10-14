# 극장의 한 줄에는 자리가 N개가 있다. 서로 인접한 좌석 사이에는 컵홀더가 하나씩 있고, 양 끝 좌석에는 컵홀더가 하나씩 더 있다. 또, 이 극장에는 커플석이 있다. 커플석 사이에는 컵홀더가 없다.
# 극장의 한 줄의 정보가 주어진다. 이때, 이 줄에 사람들이 모두 앉았을 때, 컵홀더에 컵을 꽂을 수 있는 최대 사람의 수를 구하는 프로그램을 작성하시오. 모든 사람은 컵을 한 개만 들고 있고, 자신의 좌석의 양 옆에 있는 컵홀더에만 컵을 꽂을 수 있다.
# S는 일반 좌석, L은 커플석을 의미하며, L은 항상 두개씩 쌍으로 주어진다.
# 어떤 좌석의 배치가 SLLLLSSLL일때, 컵홀더를 *로 표시하면 아래와 같다.
# *S*LL*LL*S*S*LL*
# 위의 예에서 적어도 두 명은 컵홀더를 사용할 수 없다.
# ex) 9 | SLLLLSSLL --> 7

#myanswer
N = int(input())
seat = list(map(str,input()))
single = seat.count("S")
lover = int(seat.count("L")/2)
holders = single + lover + 1

count = N - (holders - single + 1 - lover) # always gives me N - 2.

print(count)

##정답
N = int(input())
seat = input()
if seat.count("LL") > 0: # 커플석이 하나라도 있을경우
  print(len(seat.replace("LL", "S")) + 1) # 싱글자리로 바꿔준다음, 총 길이(S갯수)  + 1 (맨끝컵홀더 하나)만큼 마실수있고,
else: # 커플석이 없는경우
  print(N) # 모두 마실수 있다.
