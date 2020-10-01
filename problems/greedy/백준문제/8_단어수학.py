#민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.
# 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.
# 예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.
# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

###my trial###
#가장 긴 입력문장을 찾아, 알파벳 하나마다 9-0의 숫자를 가장높은자리수 부터 주고난뒤 입력 문장들을 다 더하려 했음.
n = int(input())
words = []
for _ in range(n):
  words.append(input())
longest = words[0]
result = 0
j = 0
arr = dict()
for i in range(n):
  words.sort(key = len, reverse=True)
  for letter in words[i]:
    arr[letter] = str(int(9-j))
    j += 1
    num = 10 ** len(words[i])-j
    # result += int(letter) * int(num)  
print(arr)


#입력받은 각 단어들이 위치한 자릿수를 각 알파벳마다 기록해준다.
# 예를 들어, ABC = A*100 + B*10 + C*1이다.
# 그럼 alphabet[A] = 100, alphabet[B] = 10, alphabet[C] = 1 이 되는 것이다.
# 이런 식으로 ABC + BCA를 한다고 해보자. 그러면 alphabet리스트의 A, B, C의 값은 다음과 같을 것이다.
# alphabet[A] = 101
# alphabet[B] = 110
# alphabet[C] = 011
# 이 값들을 내림차순으로 정렬해준 다음, 큰 값부터 작은 값으로 9부터 0까지 맵핑시켜주면 최댓값을 구할 수 있다.
# 따라서 9*110 + 8*101 + 7*11 = 1875라는 최댓값을 얻게 된다.
# ex) 2 | ABC | BCA
n = int(input()) 
word = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(n)] # A = 0 , B = 1 ...Z =25 로 단어의 각 알파벳들을 숫자로 변환해 받아줌.
alpha = [0] * 26 # 알파펫 (A-Z) 26개 들어갈 리스트 초기화 

for i in range(n):
    j = 0
    for w in word[i][::-1]: #각 알파벳에 부여된 숫자에대해, same list in reverse order:[::-1] A0 B1 C2 -> 2 1 0
        alpha[w] += (10**j) # 각 자리 알파벳에 뒤에서 부터 자릿수 일십백천.. 책정  alpha[2] += 10^0, alpha[1] += 10^1
        j += 1
alpha.sort(reverse=True) # 각문자열에 들어있던 알파벳에 지정된 자리수를 모아 더해주면, ABC+BCA = alphabet[A] = 101, alphabet[B] = 110, alphabet[C] = 11. 이를 내림차순으로 정리하면 [110, 101, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 이고 즉, B에 가장높은 수(9)를 곱해주어야 결과가 최대값이 나온다. 

answer = 0
t = 9
for i in range(26): # 모든 알파벳리스트에 대하여
    if alpha[i] == 0: # 만약 알파벳리스트 자리에 들어오지 않은부분은 삭제.
        break
    answer += (t * alpha[i]) # 가장 높은 수(t = 9)부터 하나씩 내려가며 각 알파벳이 가지고있는 자릿수를 곱해준뒤 합해준다. 
    t -= 1

print(answer)
