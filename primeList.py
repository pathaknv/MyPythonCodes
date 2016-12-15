import prime;
cnt = 0;
for i in range(2,10000):
    x=prime.primeFinder(i);
    if x == 1:
        print(i);
        cnt+=1;
print('Total Prime Numbers are ' , cnt);
