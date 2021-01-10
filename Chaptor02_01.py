#chaptor02-01 파이썬 기초
#print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

#기본출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')

print()

#separator 옵션 : 개별 문자열을 붙인다.
print('P','Y','T','H','O','N', sep='')
print('010', '7777', '1234', sep="-")
print('python','gmail.com',sep='')

#end 옵션 : 서로다른 열을 하나로 붙인다.

print('welcome to', end=' ')
print('IT News', end=' ')
print('Web site')
print()


#file 옵션

import sys
#print('Learn Python', file='sys.stdout')
#print()


#format 사용(d :정수, s :문자, f :소수)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one', 'two'))

print('%s %s' % ('stock','option'))
print('{} {}'.format('stock','option'))
print('{1} {0}'.format('stock','option'))

print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))
#_문자 채우기 ^중앙정렬
print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

#. 절삭
print('%5s' % ('nice'))
print('%.5s' % ('nice'))
print('%.5s' % ('python study'))
print('{:10.5}'.format('python study'))

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('%.4d' % (42))
print('{:4d}'.format(421111))
print('%10d' % (13))
print('%-10d' % (13))
print('{:>10d}'.format(42))

# %f
print('%f' %(3.1434343434))
print("%1.10f" % (3.1434343434))
print('{:f}'.format(3.1434343434))
print('%06.2f' % (3.1415925632125))
print('%6.2f' % (3.1415925632125))
print('{:06.2f}'.format(3.1415925632125))
