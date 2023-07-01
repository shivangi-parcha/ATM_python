user=["shivangi"]
amount=[5000]
pin=[7289]
num=[9540]
a=input("Enter your name:")
if a in user:
    b=int(input("Choice any option: 1.Balance detail" 
                "2.withdrow amount" 
                "3.Deposite amount" 
                "4.Reset Password:"))
    if b==1:
        b1=int(input("Enter your pin: "))
        if b1==pin[0]:
            amount=amount[0]
            print("Total amount available in your account is:", amount)
        else:
            print("you have entered wrong pin")
    elif b==2:
        c=int(input("Enter your amount that you want to windrow 100,200,500:"))
        c1=int(input("Enter your pin: "))
        if c1==pin[0]:
            if c<amount[0]:
                amount=amount[0]-c
                print("Total balance", amount)
                print(c)
            elif c>amount[0]:
                print("you have enter the wrong amount:")
        else:
            print("you have entered the wrong pin:")
    elif b==3:
        d=int(input("Enter your amount that you want to deposite: "))
        d1=int(input("Enter your pin"))
        if d1==pin[0]:
            amount=amount[0]+d
            print(amount)
        else:
            print("you have entered a wrong pin")
    elif b==4:
        e=int(input("Enter your security code: "))
        if e==num[0]:
            e1=int(input("Enter you new pin: "))
            e2=int(input("Enter your new pin again: "))
            if e1==e2:
                pin[0]=e1
                print(pin[0])
            else:
                print("you pin is not matched")
    

        


        