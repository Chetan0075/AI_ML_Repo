print("Welcome To Predicition System")

def menu():
    print("1. Predicition")
    print("2. View Predicition")
    print("3. Exit")

    op = input("Enter Your Choice :")
    if(op=="1"):
        prediction()

    elif(op=="2"):
        viewpredicition()

menu()        


def prediction():
    sem1 = int(input("Enter Your First Sem Marks"))
    sem2 = int(input("Enter Your Second Sem Marks"))
    sem3 = int(input("Enter Your Third Sem Marks"))
    sem4 = int(input("Enter Your Four Sem Marks"))


def viewpredicition():
    print("")


def exit():
    print("Thank You For Visiting Our Predidction System")

