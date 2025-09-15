import sys
def main():
    print("========WELCOME TO BANK========")
    x=choice()
    if x==1:
        y=int(input("Enter Amount"))
        print(add(y))
    elif x==2:
        y=input("Enter Amount")
        print(sub(y))
    elif x==3:
        print(bal())
    elif x==4:
        sys.exit("Thanks for visiting the bank 😊")



def choice():
    print("Select Operation:\n1.ADD MONEY\n2.WITHDRAW MONEY\n3.CHECK BALANCE\n4.EXIT\nEnter Choice:")
    a=int(input())
    if a not in[1,2,3,4]:
        print("Enter a valid choice")
        return choice()
    else:return a


def add(y):
    try:
        with open("bal.txt", "r") as f:
            content = f.read().strip()
            balance = int(content)
        x=int(y)+int(balance)
        with open("bal.txt", "w") as f:
            f.write(str(x))
        return(f"After adding balance is {x}")
    except:sys.exit("Wrong Input\n EXIT")

def sub(y):
    try:
        with open("bal.txt", "r") as f:
            content = f.read().strip()
            balance = int(content)
        x=int(balance)-int(y)
        with open("bal.txt", "w") as f:
            f.write(str(x))
        return(f"After subtracting balance is {x}")
    except:
        sys.exit("Invalid input\n EXIT")

def bal():
    with open("bal.txt", "r") as f:
            content = f.read().strip()
            balance = int(content)
    return (f"The balance is {balance}")



if __name__ == "__main__":
    main()