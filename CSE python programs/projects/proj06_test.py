import proj06_stringlib

test = "derpachu"
test1 = proj06_stringlib.is_alpha(test)
print(test, "is alpha", test1)

test = "d3rpachu"
test2 = proj06_stringlib.is_alpha(test)
print(test, "is alpha", test2)

test = "7331"
test3 = proj06_stringlib.is_digit(test)
print(test, "is digit", test3)

test = "L331"
test4 = proj06_stringlib.is_digit(test)
print(test, "is digit", test4)

test = "ThiS Is A TeSt"
test5 = proj06_stringlib.to_lower(test)
print(test, "to lower", test4)

test = "thIs iS a tesT"
test5 = proj06_stringlib.to_lower(test)
print("blank", "to lower", test5)

test = "THIS IS A TeST"
test6 = proj06_stringlib.to_upper(test)
print("blank", "to upper", test6)

test = "tHIS iS a tEsT"
test7 = proj06_stringlib.to_upper(test)
print(test, "to upper", test7)

x = "this is a test"
y = "i"
test8 = proj06_stringlib.find_chr(x,y)
print(1,2, "find chr", test8)

x = "this is a test"
y = "is a"
test9 = proj06_stringlib.find_str(x,y)
print(1,2, "find str", test9)

x = "this is a test"
y = "is"
test14 = proj06_stringlib.find_chr(x,y)
print(1,2, "find chr", test14)

x = "this is a test"
y = ""
test15 = proj06_stringlib.find_str(x,y)
print(1,2, "find str", test15)

x = "this is a test"
y = "i"
z = "I"
test10 = proj06_stringlib.replace_chr(x,y,z)
print(1,2,3, "replace chr", test10)

x = "this is a test"
y = "is a"
z = "isnt"
test11 = proj06_stringlib.replace_str(x,y,z)
print(1,2,3, "replace str", test11)

x = "this is a test"
y = "i"
test12 = proj06_stringlib.trim_chr(x,y)
print(1,2, "trim chr", test12)

x = "this is a test"
y = "is a"
test13 = proj06_stringlib.trim_all(x,y)
print(1,2, "trim all", test13)
