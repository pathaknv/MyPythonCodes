import amstrong;

for i in range(1,10000):
    status = amstrong.isAmstrong(i);
    if status == 1:
        print(i);
