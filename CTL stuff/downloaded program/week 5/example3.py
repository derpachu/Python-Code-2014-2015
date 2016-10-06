fd = open("out.txt", "w")
for n in range(500):
    print( "On iteration:", n, file = fd )


fd.close()
