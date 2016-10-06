in_file = open( "text.txt" )
out_file = open( "out.txt","w")

line_num = 1

for line in in_file:
    line = line.rstrip()
    print('{:2d} {:s}'.format(line_num, line,), file=out_file )
    line_num += 1

in_file.close()
out_file.close()
