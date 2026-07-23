n = 4
for i in range(0, n):
    print(i)



cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")


var = 10
for i in range(10):
    for j in range(2,10,1): #loop from 2 to  10 with the gap of 1.
        if var % 2 == 0:
            continue
        else:
            var += 1
print(var)