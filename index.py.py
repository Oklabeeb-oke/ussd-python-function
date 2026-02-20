ussd = input ("Enter your ussd code: ")
if ussd == "*312#":


    def ussd():
        print("""
            1. Data plans
            2. Recharge
            0. Exit
            """)
        option = input("Enter your option: ")
        if option == "1":
            data_plans()
        elif option == "2":
            recharge()
        elif option == "0":
            exit()
        else:
            print("Invalid option")
            ussd()
            
                

def data_plans():
    print("""
        Buy data plans
        1. Daily data plans
        2. Weekly data plans
        3. Monthly data plans
        0. Back
        """)
    option = input("Enter your option: ")
    if option == "1":
        daily_data()
    elif option == "2":
        weekly_data()
    elif option == "3":
        monthly_data()
    elif option == "0":
        ussd()
    else:
        print("Invalid input")
        data_plans()
    

def daily_data():
    print("""
        For daily data plans
        1. N75 = 75MB
        2. N100 = 110MB
        3. N350 = 500MB
        4. N1000 = 3.5GB
        0. back
        """)
    option = input("Enter your option: ")
    if option == "1":
        print("Your data subscription of 75MB for N75 is successful.")
    elif option == "2":
        print("Your data subscription of 110MB for N100 is successful.")
    elif option == "3":
        print("Your data subscription of 500MB for N350 is successful.")
    elif option == "4":
        print("Your data subscription of 3.5GB for N1000 is sucessful.")
    elif option == "0":
        data_plans()
    else:
        print("Invalid option")
    ussd()


def weekly_data():
    print("""
        For Weekly data plans
        1. N750 = 1.2GB + 1hr(IG/TT/YT)
        2. N500 = 500MB
        3. N800 = 1GB
        4. N2000 = 6GB
        0. Back
        """)
    option = input("Enter your option: ")
    if option == "1":
        print("Your data subscription of 1.2GB + 1hr(IG/TT/YT) for N750 is successful.")
    elif option == "2":
        print("Your data subscription of 500MB for N500 is successful.")
    elif option == "3":
        print("Your data subscription of 1GB for N800 is successful.")
    elif option == "4":
        print("Your data subscription of 6GB for N2000 is successful.")
    elif option == "0":
        data_plans()
    else:
        print("Invalid option")
    ussd()


def monthly_data():
    print("""
        For monthly data plans
        1. N1500 = 2GB + 2GB
        2. N2000 = 2.7Gb + 2GB
        3. N3500 = 7GB + 3GB
        4. N5000 = 14.5GB
        0. Back
        """)
    option = input("Enter your option: ")
    if option == "1":
        print("Your data subscription of 2GB + 2GB for N1500 is successful.")
    elif option == "2":
        print("Your data subscription of 2.7GB + 2GB for N2000 is successful.")
    elif option == "3":
        print("Your data subscription of 7GB + 2GB for N3500 is successful.")
    elif option == "4":
        print("Your data subscription of 14.5GB for N5000 is successful.")
    elif option == "0":
        data_plans()
    else:
        print("Invalid option")
    ussd()


def recharge():
    print("""
        PLEASE SELECT
        1. Self
        2. Third Party
        0. Back
        """)
    option = input("Enter your option: ")
    if option == "1":
        self_recharge()
    elif option == "2":
        third_party_recharge()
    elif option == "0":
        ussd()
    else:
        print("Invalid option")
        recharge()


def self_recharge():
    print("""
        PLEASE ENTER AMOUNT
        00. Back
        """)
    amount = input("Enter your amount or 00 to go back: ")
    if amount != "00":
        print(f"Your recharge of #{amount} is successful.")
        ussd()
    else:
        recharge()


def third_party_recharge():
    print("""
        PLEASE ENTER THE THIRD PARTY MOBILE NUMBER
        00. Back
        """)
    number = input("Enter the third party mobile number or 00 to go back: ")
    if len(number) == 11 and number.isdigit:
        if number[:3] in ["070", "071", "080", "081", "090", "091"]:
            print("PLEASE ENTER AMOUNT")
            amount = input("enter your amount: ")
            print(f"Your recharge of #{amount} for {number} is successful.")
            ussd()
        else:
            print("Invalid Phone Number")
            third_party_recharge()
    elif number == "00":
        recharge()
    else:
        print("Wrong Number")
        third_party_recharge()
        

ussd()
