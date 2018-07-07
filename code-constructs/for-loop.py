size = 7

for i in range(size):
    print("%2d -" % (i + 1), "*" * (i + 1))
    
for i in range(size):
    print("%2d - " % ((size - 1) - i), " " * ((size - 1) - i),"*" * (i + 1), sep = "")
