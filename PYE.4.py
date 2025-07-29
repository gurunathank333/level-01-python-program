print ("       Guru Supermarket")
print ("No 7, Grandhi Nagar Acharapakkam")
print ("-----------------")
print ("  Bill Receipt")
print ("-----------------")
input("enter the serial number:")
input("enter the partculars :")
rate=int(input("enter the rate:"))
quantity=int(input("enter the quantity:"))
total=rate*quantity
print ("Total Amount RS:", total)
gst=total*10/100
print("gst(10per) :",gst)
paid=total+gst
print("Amout to be paid Rs :",total)
