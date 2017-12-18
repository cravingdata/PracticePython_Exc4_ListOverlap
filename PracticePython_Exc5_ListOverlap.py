a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = a + b

print c

print "old list of list c length: %s" % len(c)
index = 0
index2 = 0
d = []
for value in c:
    print c[index]
    num = 0
    #making index2 xero here in loop forces index2 to start at 0
    #when last if ends
    index2 = 0
    if index < len(c) - 1:
        print index
        print c[index]
        for num in c:
            if c[index] == c[index2] and index != index2:
                print "c[index] is: %s" % c[index]
                print "index %s" % index
                print "index2 %s" % index2
                print "c[index2] is: %s" % c[index2]
                c.remove(c[index2])

            index2 = index2 + 1
    index = index + 1

print
print "list c: %s" % c
print "new length of list c: %s" % len(c)
