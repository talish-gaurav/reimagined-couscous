try:
   num = int(input("Enter a number"))
   if num%2==0:
    print("Number is even")
   else:
    raise ValueError
except ValueError:
    print("Re-enter a number divisible by 2")