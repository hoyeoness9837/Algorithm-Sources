#다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
#input = 12345
#output 
# [10000]
# [2000]
# [300]
# [40]
# [5]

a, b, c, d, e = input()

print('[%d]' % (int(a)*10000))
print('[%d]' % (int(b)*1000))
print('[%d]' % (int(c)*100))
print('[%d]' % (int(d)*10))
print('[%d]' % int(e))


#solution
n=input()

print( "[" + str( int(n[0]) * 10000 ) + "]" )
print("["+str(int(n[1])*1000)+"]")
print("["+str(int(n[2])*100)+"]")
print("["+str(int(n[3])*10)+"]")
print("["+str(int(n[4]))+"]")