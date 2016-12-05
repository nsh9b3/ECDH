a = 4
b = 15
s = 0
old_s = 1
t = 1
old_t = 0
r = b
old_r = a
while r != 0:
	quotient = old_r // r
	old_r, r = r, old_r - quotient * r
	old_s, s = s, old_s - quotient * s
	old_t, t = t, old_t - quotient * t

inv = old_s
if inv < 0:
	inv = b + inv
if old_r == 1:
	print 'solution is {}'.format(inv)
else:
	print 'No inverse'