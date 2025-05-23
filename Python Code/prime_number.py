a = int(input("Enter a number: "))

for n in range(2, a):
    if (a%n) == 0 :
        print(f"{a} is not a prime number")
        break
else: 
    print(f"{a} is  a prime number")
