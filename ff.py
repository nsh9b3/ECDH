def finiteField():
    def inv(self, n, p):
		s, old_s = 0, 1
		t, old_t = 1, 0
		r, old_r = p, n
		while r != 0:
			quotient = old_r // r
			old_r, r = r, old_r - quotient * r
			old_s, s = s, old_s - quotient * s
			old_t, t = t, old_t - quotient * t

		inv = old_s
		if inv < 0:
			inv = b + inv
		if old_r == 1:
			return inv
		else:
			return -1