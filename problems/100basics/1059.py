#비트 단위로 1 -> 0, 0 -> 1로 바꾼 후 그 값을 10진수로 출력한다.
# ~n = - n -1
a = int(input())
b = -(a)-1
print(b)

#solution
a=input()
n=int(a)
print(~n)


#bit = '{0:08b}'.format(a)
#1. {} places a variable into a string
#2. 0 takes the variable at argument position 0
#3. : adds formatting options for this variable (otherwise it would represent decimal 6)
#4. 08 formats the number to eight digits zero-padded on the left
#5. b converts the number to its binary representation
#integer = int(bit, base = 2)