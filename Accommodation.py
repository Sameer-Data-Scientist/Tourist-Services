import random as rd


def room_no():
    room = int(input(""" View your room: 
    Check Room On Your Choice >>>> 
    Range of Room-number's in Hotel is (1 to 300)
    Enter any room no and check if it's free or not >>> 
    """))
    a="Room Already Book \n  Choice Another "
    b="Room is Free"
    d=rd.choice([a,b])
    if d==a:
            print(a)
            print(room_no())
    else:
            print(d)
    return " "

def hotel(a):
        c = input("Select any one : 1 / 2 / 3")
        if c == "1":
                print(" Your Hotel is ", a[0])
                print(room_no())
        elif c == "2":
                print(" Your Hotel is ", a[1])
                print(room_no())
        elif c == "3":
                print(" Your Hotel is ", a[2])
                print(room_no())
        else:
               print(" hotel is not available ")
        return " Okay "
def view_dishes(l):
        print("Here the list of food is :")
        for i in range(len(l)):
                print(l[i])
        return ""
def choose(li):
        ch = input("Enter Code ?  ")
        q=int(input("How Much Quantity... Much at least (1)  "))

        if ch == "1":
                print("Now Your Order is", li[0],"Total Price in PKR is :",2500*q)
        elif ch == "2":
                print("Now Your Order is", li[1],"Total Price in PKR is :",2589*q)
        elif ch == "3":
                print("Now Your Order is", li[2],"Total Price in PKR is :",1499*q)
        elif ch == "4":
                print("Now Your Order is", li[3],"Total Price in PKR is :",5000*q)
        elif ch == "5":
                print("Now Your Order is", li[4],"Total Price in PKR is :",3999*q)
        else:
                return "Choose Only Above Dishes"

def meal():
        book=input(" Do you want to eat special thing's of this Hotel ? (y/n)").lower()
        if book=="y":
                print("Here is Some Special Dishes For you ..")
                l=["1. Chinese Dishes",
                "2. Desi Dishes",
                "3. BBQ Dishes",
                "4. Continental Dishes",
                "5. Fast Food "]
                for i in range(len(l)):
                        print(l[i])
                m=input("What you want to Choose ..."
                        "Enter Code ?    ")
                if m=="1":
                        li=["1.Chicken Manchurian (2500)",
                        "2.Chicken/Beef Chow Mein (2589)" ,
                        "3.Chicken Fried Rice (1499)",
                        "4.Hot and Sour Soup (5000)",
                        "5.Szechuan Chicken (3999)"]
                        print(view_dishes(li))
                        print(choose(li))
                elif m=="2":
                        li = ["1.Chicken Karahi (2500)",
                              "2.Mutton Handi (2589)",
                              "3.Beef Nihari (1499)",
                              "4.Daal Makhani (5000)",
                              "5.Tandoori Chicken (3999)"]
                        print(view_dishes(li))
                        print(choose(li))
                elif m=="3":
                        li = ["1.Seekh Kebab (2500)",
                              "2.Chicken/Mutton Boti (2589)",
                              "3.Malai Boti (1499)",
                              "4.Behari Kebab (5000)",
                              "5.Grilled Fish (3999)"]
                        print(view_dishes(li))
                        print(choose(li))
                elif m=="4":
                        li = ["1.Grilled Chicken Steak (2500)",
                              "2.Alfredo Pasta (2589)",
                              "3.Chicken Cordon Bleu (1499)",
                              "4.Club Sandwich (5000)",
                              "5.Cream of Mushroom Soup (3999)"]
                        print(view_dishes(li))
                        print(choose(li))
                elif m=="5":
                        li = ["1.Zinger Burger (2500)",
                              "2.Shawarma (2589)",
                              "3.Crispy Fried Chicken (1499)",
                              "4.Pizza (Pakistani-spiced toppings) (5000)",
                              "5.Loaded Fries (3999)"]
                        print(view_dishes(li))
                        print(choose(li))
                else:
                      print("Choose from above...")
        else:
                return "Thank's "



def hotels_book():
        while True:
                a = input(" Welcome to \" Booking services for hotels\" \n"
                          "In Which City Do You want ?\n"
                          """Here are some popular cities in Pakistan for hotel booking:

                1. Karachi 
                2. Lahore  
                3. Islamabad  
                4. Murreeh
                5. Peshawar  
                6. Rawalpindi  
                7. Faisalabad  
                8. Multan  
                9. Quetta  
                """)
                print("Here Some Hotel's  ....".center(100, "~"))
                if a == "1":
                        b = ["1.Mövenpick Hotel Karachi", "2.Pearl Continental Hotel Karachi", "3.Marriott Karachi"]
                        print(b[0], "\n", b[1], '\n', b[2])
                        print(hotel(b))
                        print(meal())
                elif a == "2":
                        b = ["1.Pearl Continental Hotel Lahore", "2.Pearl Continental Hotel Bhurban",
                             "3.Pearl Continental Hotel Rawalpindi"]
                        print(b[0], "\n", b[1], '\n', b[2])
                        print(hotel(b))
                        print(meal())


                elif a == "3":
                        b = ["1.Serena Hotel Islamabad", "2.Pearl Continental Hotel Islamabad",
                             "3.Marriot Hotel Islamabad"]
                        print(b[0], "\n", b[1], '\n', b[2])
                        print(hotel(b))
                        print(meal())

                elif a == "4":
                        b = ["1.PC Bhurban", "2.Mirpur Guest House", "3.Neelum View Resort"]
                        print(b[0], "\n", b[1], '\n', b[2])
                        print(hotel(b))
                        print(meal())

                elif a == "5":
                        b = ["1.Pearl Continental Hotel Peshawar", "2.Pearl Continental Hotel Rawalpindi",
                             "3.Pearl Continental Hotel Gilgit"]
                        print(b[0], "\n", b[1], '\n', b[2])
                        print(hotel(b))
                        print(meal())

                elif a == "6":
                        b = ["1.Pearl Continental Hotel Rawalpindi", "2.Serena Hotel Rawalpindi",
                             "3.Sangam Hotel Rawalpindi"]
                        print(b[0], "\n", b[1], '\n', b[2])
                        print(hotel(b))
                        print(meal())

                elif a == "7":
                        b = ["1.ChenOne Tower", "2.The Nishat Hotel Faisalabad", "3.Serena Hotel Faisalabad"]
                        print(b[0], "\n", b[1], '\n', b[2])
                        print(hotel(b))
                        print(meal())

                elif a == "8":
                        b = ["1.Pearl Continental Hotel Multan", "2.TNew Shaheen Hotel", "3.Faletti's Hotel"]
                        print(b[0], "\n", b[1], '\n', b[2])
                        print(hotel(b))
                        print(meal())

                elif a == "9":
                        b = ["1.Serena Hotel Quetta", "2.The Clifton Hotel Quetta", "3.Sanghar Hotel"]
                        print(b[0], "\n", b[1], '\n', b[2])
                        print(hotel(b))
                        print(meal())

                else:
                        return " Choose correct option ...."
                g=input(" Do you want to View more hotel's ? (y/N)").lower()
                if g=="n" or g=="N":
                        break




