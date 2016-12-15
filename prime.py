import math

def primeFinder(x):

  i = 3;
  if x == 2:
      return 1;
  if x%2 == 0:
      return 0;
  while i <= math.sqrt(x):
      if x%i == 0:
          return 0;
      i+=2;
  return 1;

x=primeFinder(15);
if x == 1:
    print('Prime Number');
else:
    print('Not Prime Number');