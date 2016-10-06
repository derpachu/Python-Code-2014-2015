import clock

A = clock.time(1, 1, 30)
print(A)
B = clock.time()
B.from_str("1:1:30")
print(B)
