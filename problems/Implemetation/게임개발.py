## Question ##

# 현재위치에서 현재 방향을 기준으로 왼쪽방향 반시계방향으로 90도 회전하며 차ㅓ례대로 갈곳을 정한다. 아직 가보지 않은 칸이 존재하면 왼쪽방향으로 회전후 앞으로 한간 전진한다. 찾을때 까지 회전하다가 다 막혔거나 가봤을경우. 방향을 유지한채로 뒤로 가본다, 뒤에도 만약 가봤다면, 움직임을 멈춘다.
# 북 0 동 1 남 2 서 3 를 방향으로 정하고 육지는 0 바다는 1로 정한다
# 첫째 줄에 이동을 마친후 캐릭터가 방문한 칸의 수를 출력한다.
# 인풋 = 첫 시작 맵크기  n * m, 시작점과 방향 a, b, direction.
# INPUT = 4 4 | 1 1 0 | 1 1 1 1 | 1 0 0 1 | 1 1 0 1 | 1 1 1 1
# ANSWER = 3


## My Answer
# COUlDN'T SOLVE...

## Solution 1
n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)


## Notes ##