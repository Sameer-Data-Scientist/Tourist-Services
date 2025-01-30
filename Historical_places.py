def region(b,re):

    if b == 1:
        print(re[1])
    elif b == 2:
        print(re[2])
    elif b == 3:
        print(re[3])
    elif b == 4:
        print(re[4])
    elif b == 5:
        print(re[5])
    elif b == 6:
        print(re[6])
    elif b == 7:
        print(re[7])
    elif b == 8:
        print(re[8])
    elif b == 9:
        print(re[9])
    elif b== 10:
        print(re[10])
    else:
        print("Wrong Choose")
def punjab():
    print("Here is the Cities of Punjab...")
    b = int(input(""" Choose Punjab City Code ....

        1. Lahore 
        2. Faisalabad
        3. Rawalpindi
        4. Multan
        5. Gujranwala
        6. Sialkot
        7. Sargodha
        8. Bahawalpur
        9. Sheikhupura
        10. Jhelum

        """))
    print("Here The Historical Places ... ")
    punj = {1: """
    Badshahi Mosque (1673)
    Lahore Fort (Shahi Qila) (UNESCO World Heritage Site)
    Minar-e-Pakistan (Symbol of Pakistan Resolution)
    Shalimar Gardens (Mughal era, UNESCO World Heritage Site)
    Tomb of Jahangir (17th-century Mughal emperor)
    Walled City of Lahore (13 historic gates and old bazaars)""",
            2: """
    Clock Tower (Ghanta Ghar) (built in 1903, iconic landmark)
    Lyallpur Museum (showcasing the city’s history and culture)
    D Ground Park (a historic commercial and recreational area)
    Chenab Club (British colonial-era building)""",
            3: """
    Rawat Fort (16th century, built by the Gakhar tribe)
    Gurdwara Panja Sahib (important Sikh pilgrimage site)
    Shah Chan Chiragh (historical shrine)
    Lal Haveli (historic building from the pre-partition era)""",
            4: """
    Tomb of Shah Rukn-e-Alam (built in 1324, iconic Sufi shrine)
    Tomb of Bahauddin Zakariya (Sufi saint of the 13th century)
    Multan Fort (Qasim Bagh Fort) (historic site with ancient ruins)
    Hussain Agahi Bazaar (one of the oldest bazaars in Pakistan)""",
            5: """
    Sheranwala Bagh (historic garden and park)
    Gurdwara Rori Sahib Eminabad (significant Sikh site)
    Gujranwala Baradari (Mughal-era pavilion)
    Ghanta Ghar (Clock Tower) (British colonial-era structure)""",
            6: """
    Iqbal Manzil (birthplace of Allama Iqbal, philosopher and poet)
    Sialkot Fort (believed to be 2,000 years old)
    Shivala Teja Singh Temple (Hindu temple)
    Sialkot Cathedral (built during the British era)""",
            7: """
    Sargodha Airbase Monument (commemorates the 1965 Indo-Pak war)
    Kirana Hills (ancient hills with archaeological significance)
    Tombs of Sufi Saints (various shrines of local saints)""",
            8: """
    Noor Mahal (19th-century Italian-style palace)
    Derawar Fort (9th-century fort in the Cholistan Desert)
    Abbasi Mosque (built by Nawab Sadiq Khan in 1849)
    Darbar Mahal (royal palace from the era of Nawabs)
    Uch Sharif (ancient city with historic Sufi shrines)""",
            9: """
    Hiran Minar (built by Emperor Jahangir in 1606)
    Sheikhupura Fort (built during the Mughal era)
    Jandiala Sher Khan (birthplace of famous Punjabi poet Waris Shah)""",
            10: """
    Rohtas Fort (UNESCO World Heritage Site, built by Sher Shah Suri)
    Tilla Jogian (ancient Hindu and Buddhist pilgrimage site)
    Alexandria Monument (marks the location of Alexander the Great’s crossing of the Jhelum River)
    Mangla Dam (historic dam and lake with ancient surroundings)"""}
    print(region(b,punj))

    return " Thank's For Visiting ".center(100, "~")

def Sindh():
    print("Here the cities of Sindh...")
    b = int(input(""" Choose Sindh City Code ....
        1.Karachi 
        2.Hyderabad
        3.Sukkur
        4.Larkana
        5.Nawabshah (Shaheed Benazirabad)
        6.Mirpur Khas
        7.Khairpur
        8.Thatta
        9.Jacobabad
        10.Umerkot"""))
    print("Here The Historical Places >>>>....")
    sindh = {1: """  
        Quaid-e-Azam Mausoleum (Mazar-e-Quaid) (tomb of Muhammad Ali Jinnah)
        Mohatta Palace (built in 1927, now a museum)
        Frere Hall (Victorian-era building from 1865)
        Empress Market (British colonial-era market)
        Chaukhandi Tombs (ancient Islamic cemetery with intricate carvings)
        Wazir Mansion (birthplace of Quaid-e-Azam)""",
             2: """
        Pakka Qila (Fort) (built by Mian Ghulam Shah Kalhoro in the 18th century)
        Tombs of Talpur Mirs (historical tombs of the Talpur rulers)
        Rani Bagh (historical garden and zoo)
        Sindh Museum (showcasing Sindh’s history and culture)""",
             3: """
        Sukkur Barrage (built during British rule in 1932)
        Sadhu Bela Temple (a historic Hindu temple on an island in the Indus River)
        Lansdowne Bridge (historic bridge built in 1889)
        Masoom Shah Minaret (17th-century watchtower)""",
             4: """
        Mohenjo-daro (UNESCO World Heritage Site, ancient Indus Valley Civilization)
        Chandka Fort (ancient fort near the city)
        Ali Wahan (archaeological site of the Indus Valley Civilization)""",
             5: """
        Sufi Shrines (various shrines of local saints, including Syed Sadaruddin Shah)
        Jam Sahib (old village with historical significance)""",
             6: """
        Khaan Garden (built during the Talpur dynasty)
        Shiv Mandir (ancient Hindu temple)
        Mir Sher Muhammad Talpur Tomb (a historical tomb of the Talpur ruler)""",
             7: """
        Faiz Mahal (19th-century palace of the Talpur rulers)
        Kot Diji Fort (pre-Indus Valley Civilization fort)
        Shrine of Sachal Sarmast (Sufi poet and saint)
        Tombs of Sohrab Khan (ancient tombs of local rulers)""",
             8: """
        Makli Necropolis (UNESCO World Heritage Site, one of the largest graveyards in the world)
        Shah Jahan Mosque (built during the Mughal era in 1647)
        Keenjhar Lake (associated with the folklore of Noori Jam Tamachi)
        Banbhore (ancient port city, believed to be the site of early Arab invasions)""",
             9: """
        Tomb of General John Jacob (founder of Jacobabad, built in 1858)
        Jamia Masjid (British-era mosque with unique architecture)
        Victoria Clock Tower (built during the colonial era)""",
             10: """
        Umerkot Fort (birthplace of Emperor Akbar, built in the 11th century)
        Shrine of Udero Lal (significant to both Hindus and Muslims)
        Akbari Mosque (built during the reign of Akbar)"""}
    print(region(b,sindh))
    return " Thank's For Visiting ".center(100, "~")
def kpk():
    print("Here is the Cities of KPK...")
    b = int(input(""" Choose the KPK City  Code ....
        1.Peshawar
        2.Abbottabad
        3.Swat (Mingora)
        4.Mardan
        5.Mansehra"""))
    print( " Historical Places.. >>>>    ")
    KPK = {1: """
        Bala Hissar Fort
        Mahabat Khan Mosque
        Qissa Khwani Bazaar
        Jamrud Fort
        Gor Khatri""",
           2: """
        Ilyasi Mosque
        Shimla Hill
        St. Luke’s Church""",
           3: """
        Butkara Stupa
        Swat Museum
        Udegram Buddhist Monastery
        Malakand Fort""",
           4: """
        Takht-i-Bahi (UNESCO World Heritage Site)
        Jamal Garhi Buddhist Monastery
        Sawaldher Stupa""",
           5: """
        Ashoka Rock Edicts
        Hazara University Museum
        Shinkiari Fort"""}
    print(b,KPK)
    return " Thank's For Visiting ".center(100, "~")
def balochistan():
    print("Here is the Cities of Balochistan ...")
    b = int(input(""" Choose Your Place Code ....
        1. Quetta
        2. Gwadar
        3.Makran Coast
        4.Khuzdar
        5.Chaman"""))
    print("Here The Historical Places >>>>....")
    bal = {1: """
        Khojak Pass
        Quetta Archaeological Museum
        Hanna Lake
        Ziarat Juniper Forest
        Mastung""",
           2: """
        Gwadar Fort
        Hingol National Park
        Sphinx of Balochistan
        Balochistan Coastal Line""",
           3: """
        Hingol National Park
        Princess of Hope
        Buzzi Pass""",
           4: """
        Kirthar National Park
        Hinglaj Mata Temple
        Mountains of Khuzdar""",
           5: """
        Chaman Border
        Spin Boldak"""}
    print(region(b,bal))
    return " Thank's For Visiting ".center(100,"~")


def historical_place():
    print(" \n Welcome to Historical Places Finder ".center(100, "*"))
    while True:
        a = int(input(""" In which Province are you finding...
            1. Punjab
            2. Sindh
            3. Khyber Pakhtunkhwa (KPK)
            4. Balochistan

            Enter Code Here ...
            """))
        if a == 1:
            print(punjab())

        elif a == 2:
            print(Sindh())
        elif a == 3:
            print(kpk())
        elif a==4:
            print(balochistan())
        else:
            print("Wrong Input , Please choose correct function.")

        c = input(" <Next Or Stop >").lower()
        if c == "s" or c == "stop":
            break

    return "Good-Bye".center(100,"^")
