#Computer Project #2
#Joe Tang

#inputs
#calculate the length of one side in the outer edge
#calculate the width of the border
#calculate the length of one flower bed
#mulch depth on walkways (mulch in border will be twice as deep)
#minimal distance between shrubs

#outputs
#Area of the border
#Area of the walkways
#Area of the four flower beds
#Total mulch required
#total amount of shrubs required

length_outer = float (input ("Please enter the length of the outer edge: "))
width = float (input ("Please enter the width of the border: "))
length_flower = float (input ("Please enter the length of the flower bed: "))

area_inner = length_outer-(2*width) 
area_border = length_outer**2 - (area_inner)**2
area_flower = 4*(length_flower)**2
area_walkway = area_inner**2 - area_flower

yard_border = area_border/9
yard_walkway = area_walkway/9
yard_flower = area_flower/9

area_border = round(area_border,1)
area_flower = round(area_flower,1)
area_walkway = round(area_walkway,1)
yard_border = round(yard_border,1)
yard_walkway = round(yard_walkway,1)
yard_flower = round(yard_flower,1)

print ("Border area: ", area_border, " or ", yard_border)
print ("Walkway area: ", area_walkway, " or ", yard_walkway)
print ("Flower area: ", area_flower, " or ", yard_flower)

mulch_walkways = float (input ("How deep is the mulch: "))
mulch_walkways /= 36
mulch_total = 2*(yard_border*mulch_walkways) + (yard_walkway*mulch_walkways)
mulch_total = round(mulch_total,1)

print ("Total mulch needed: ", mulch_total)


shrub_distance = float (input ("What is the minimal distance: "))

shrub_length = length_outer - width
shrub_count = shrub_line = float (1)

while shrub_line < shrub_length:
    shrub_line += shrub_distance
    shrub_count += 1
shrub_count *= 4
shrub_count -= 8

print ("Number of shrubs: ", shrub_count)
