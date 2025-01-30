import Historical_places as hps
import Voice_translator as vst
import guider_find as guf
import Accommodation as acc
print(" Welcome to Voice Translator Services for Tourist ".center(150))
print("Some Service are :.....:......:.....:")
a=["Historical Places finder"," Voice Translator "," Find Guider ","Hotel Booking","About Program","Write Your Comment About Product"]
d=1
for i in range(len(a)):
    print(d,a[i])
    d+=1
b=input(" Select 1/2/3/4/5/6       ")
if b=="1":
    print(hps.historical_place())
elif b=="2":
    print(vst.voice_translator())
elif b=="3":
    print(guf.guider_find())
elif b=="4":
    print(acc.hotels_book())
elif b=="5":
    c=open("About.txt","r")
    f=c.read()
    c.close()
    print(f)
elif b=="6":
    c=open("Comment.txt","w")
    g=input("Write Your Comment Here..")
    c.write(g)
    c.close()
    print("Your Comment:  ",g)
else:
    print("Wrong Choose")