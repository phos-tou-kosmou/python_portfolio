# Source https://en.wikipedia.org/wiki/Derangement

# !n = (n-1)(!(n-1)+!(n-2))

# We find that !0 == 1 and !1 == 0
# so when we use !n to calculate !2 we find that !2 == (2-1)(!(n-1)+!(n-2))
# well we know that n-1 == !1 which is 0 and n-2 == !0 which is 1.

# Since we know the series is finite and will converge at one point (proven by the fact that
# we are operating over a finite field F), then we may conclude that each summation is accumulating
# to a discrete value.

# !2 is defined as 1

total = []

total.append(1)
total.append(0)
total.append(1)
final = 0
n = 26

for i in range(3, n+1):
    final = (i-1)*(total[i-1] + total[i-2])
    total.append(final)

print('Permutations with no fields fixed: ', final)

nf = 1
for i in range(1, n+1):
    nf *= i

print('Permutations with one field fixed: ', nf- final)

