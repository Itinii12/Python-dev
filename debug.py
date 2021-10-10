print("main start.")

one = input("No1 =")
two = input("No2 =")
count = input("count =")

print(f"{one=},{two=}")
result = input("really exe?(y or n):")

print(f'{result=}')
if result == "y":
    for i in range(int(count)):
        print(f"{one=},{two=}")
elif result == ("No" or "n"):
    print("dont exe")
else:
    print("ERROR.")

print("main end.")
