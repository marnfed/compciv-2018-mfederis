def fob():  
    print(1,100)
for foozbuzz in range (100):
    if foozbuzz % 3 == 0 and foozbuzz % 5 == 0:
        print ("foozbuzz")
        continue
    elif foozbuzz %  3 == 0:
        print ("fooz")
        continue
    elif foozbuzz % 5 == 0:
        print ("buzz")  
        continue
    print (foozbuzz)
    