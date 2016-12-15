def isAmstrong(x) :
    tmp = x;
    check=0;
    while x > 0:
        dig = x%10;
        x = int(x/10);
        check += dig ** 3;
    if tmp == check:
        return 1;
    else:
        return 0;

status = isAmstrong(371);
if status == 1:
    print('Number is Amstrong');
else:
    print('Number is not Amstrong');