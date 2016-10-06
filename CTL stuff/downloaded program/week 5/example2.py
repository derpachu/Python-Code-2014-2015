fd = open("out.txt", "w")
print( "one", 1, file=fd )
print( "two", 2, file=fd )
fd.close()


