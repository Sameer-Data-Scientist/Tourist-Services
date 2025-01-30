import random as rd
def guider():
        b = input("""For Which City...>>>...
        1.Lahore
        2.Faisalabad
        3.Rawalpindi
        4.Multan
        5.Gujranwala


        Enter Code ...>>>

        """)
        if b == "1":
                print(" Available Member's For Lahore :")
                city = {"Ali", "Fatima", "Hassan", "Zainab", "Bilal", "Ayesha"}
                ci = rd.choice(list(city))
                print(city, "\n For You The Best Guider is ", ci)
        elif b == "2":
                print(" Available Member's For Faisalabad :")
                city = {"Ahmed", "Sara", "Umar", "Noor", "Hamza", "Kashif"}
                ci = rd.choice(list(city))
                print(city, "\n For You The Best Guider is ", ci)
        elif b == "3":
                print(" Available Member's For Rawalpindi :")
                city = {"Asma", "Rizwan", "Maryam", "Yasir", "Nida", "Kashif"}
                ci = rd.choice(list(city))
                print(city, "\n For You The Best Guider is ", ci)
        elif b == "4":
                print(" Available Member's For Multan :")
                city = {"Usman", "Hina", "MSaad", "Laiba", "Arslan", "Iqra"}
                ci = rd.choice(list(city))
                print(city, "\n For You The Best Guider is ", ci)
        elif b=="5":
                print(" Available Member's For Gujranwala :")
                city = {"Sameer", "Anam", "Imran", "Zeeshan", "Arslan", "Rabia"}
                ci = rd.choice(list(city))
                print(city, "\n For You The Best Guider is ", ci)
        else:
                print("Wrong Choose")
        d=input(" Do you want to change the Guider ? (Yes)/(NO)").lower()
        if d=="y" or d=="Yes":
                f=input(" Write The Name Of Your Guider in Available member")
                print(" Now Your Guider is ",f)



        return "Thank's For Visiting".center(100,"~")

def guider_find():
        a = input(" Welcome to  \" Find Guider For Vist\" Tour \n:"
                  "  1. City tours "
                  "  2. Historical site tours"
                  "  3. Nature or adventure tours"

                  " Enter Code>>> ")
        if a == "1":
                print("~" * 100, "\n Here ... Guider For City Tour ...")
                print(guider())

        elif a == "2":
                print("~" * 100, "\n Here ... Historical site tours ...")
                print(guider())
        elif a == "3":
                print("~" * 100, "\n Here ... Nature or adventure tours ...")
                b = input("""For Which City...>>>...
                        1.Swat
                        2.Hunza
                        3.Skardu
                        4.Naran
                        5.Gilgit


                        Enter Code ...>>>

                        """)
                if b == "1":
                        print(" Available Member's For Swat :")
                        city = {"Ali", "Fatima", "Hassan", "Zainab", "Bilal", "Ayesha"}
                        ci = rd.choice(list(city))
                        print(city, "\n For You The Best Guider is ", ci)
                elif b == "2":
                        print(" Available Member's For Hunza :")
                        city = {"Ahmed", "Sara", "Umar", "Noor", "Hamza", "Kashif"}
                        ci = rd.choice(list(city))
                        print(city, "\n For You The Best Guider is ", ci)
                elif b == "3":
                        print(" Available Member's For Skardu :")
                        city = {"Asma", "Rizwan", "Maryam", "Yasir", "Nida", "Kashif"}
                        ci = rd.choice(list(city))
                        print(city, "\n For You The Best Guider is ", ci)
                elif b == "4":
                        print(" Available Member's For Naran :")
                        city = {"Usman", "Hina", "MSaad", "Laiba", "Arslan", "Iqra"}
                        ci = rd.choice(list(city))
                        print(city, "\n For You The Best Guider is ", ci)
                elif b=="5":
                        print(" Available Member's For Gilgit :")
                        city = {"Sameer", "Anam", "Imran", "Zeeshan", "Arslan", "Rabia"}
                        ci = rd.choice(list(city))
                        print(city, "\n For You The Best Guider is ", ci)
                else:
                        print("Wrong Choose")
                d = input(" Do you want to change the Guider ? (Yes)/(NO)").lower()
                if d == "y" or d == "Yes":
                        f = input(" Write The Name Of Your Guider in Available member")
                        print(" Now Your Guider is ", f)

        return " End ".center(100,"-")
