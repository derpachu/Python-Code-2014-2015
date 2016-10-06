def draw_line(line_spec):
    """draws a line of alternating spaces and stars; line_spec (a list of ints)
       specifies the number of each character to draw, starting with spaces"""
    result = ''
    star_turn = False      
    for num in line_spec:
        if star_turn:
            result = result + num * '*'
        else:
            result = result + num * ' '
        star_turn = not star_turn
    print(result)

def draw_vee(height):
    """draws a vee of the given height (a pos int)"""
    for i in range(0, height-1):
        lspec = [i, 1, 2*(height-i)-3, 1]
        draw_line(lspec)
    draw_line([height-1, 1])
        
def draw_left_parallelogram(w, h):
    """draws a left-slanting parallelogram of the given width and height
       (both positive ints)"""
    for i in range(0,h):
        num = [i, w]
        draw_line(num)

def draw_right_parallelogram(w, h):
    """draws a right-slanting parallelogram of the given width and height
       (both positive ints)"""
    for i in range(0,h):
        num = [w-i, w]
        draw_line(num)

def draw_parallelogram(w, h, left = True):
    """draws a parallelogram of the given width and height (both pos ints);
       left slanting if left is True (the default); otherwise, right slanting"""
    if left == True:
        draw_left_parallelogram(w,h)
    if left == False:
        draw_right_parallelogram(w,h)
def draw_triangle(w):
    """draws an isosceles triangle of the given width (pos int), if it is odd;
       or of width one more than the given width, if it is even"""
    if w%2 == 1:
        for i in range(0,w//2+1):
            pattern = [w-(w//2+1+i), 2*i+1, w-(w//2+1+i)]
            draw_line(pattern)
    else:
        w += 1
        for i in range(0,w//2+1):
            pattern = [w-(w//2+1+i), 2*i+1, w-(w//2+1+i)]
            draw_line(pattern)
def draw_2ndtriangle(w):
    """draws an inverted triangle that decreses its w by 1"""
    for i in range(0,w):
        pattern = [0,w-i]
        draw_line(pattern)
def draw_invertedtriangle(w):
    """plugging the widest part of the star it increments up by 1 until reaching that point
       then decreases by 1 after the widest part"""
    for i in range(1,w+1):
        pattern = [0,i]
        draw_line(pattern)
    for i in range(1,w):
        pattern = [0,-1*i+w]
        draw_line(pattern)
def draw_hourglass(w):
    """w is the top and the bottom width that determins the triangles"""
    if w%2==1:
        for i in range(0,w//2):
            pattern = [0+i,w-2*i,0+i]
            draw_line(pattern)
    else:
        w -= 1
        for i in range(0,w//2):
            pattern = [0+i,w-2*i,0+i]
            draw_line(pattern)
    draw_triangle(w)
def draw_diamond(w):
    """w is the widest part of the diamond"""
    if w%2 == 1:
        for i in range(0,w//2):
            pattern = [w-(w//2+1+i), 2*i+1, w-(w//2+1+i)]
            draw_line(pattern)
    else:
        w += 1
        for i in range(0,w//2):
            pattern = [w-(w//2+1+i), 2*i+1, w-(w//2+1+i)]
            draw_line(pattern)
    if w%2==1:
        for i in range(0,w//2+1):
            pattern = [0+i,w-2*i,0+i]
            draw_line(pattern)
    else:
        w -= 1
        for i in range(0,w//2+1):
            pattern = [0+i,w-2*i,0+i]
            draw_line(pattern)
def test_draw_line():
    print("draw_line([0, 3, 2, 3]) prints:")
    draw_line([0, 3, 2, 3])
    print(8*'-')
    print()
    print("draw_line([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) prints:")
    draw_line([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    print(10*'-')
    print()
    print("draw_line([0, 1, 1, 2, 1, 3, 1, 2, 1, 1]) prints:")
    draw_line([0, 1, 1, 2, 1, 3, 1, 2, 1, 1])
    print(13*'-')


    
        
        

    

