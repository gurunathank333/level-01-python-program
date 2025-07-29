print("Goverment of tamilnadu")
print("-----------------------")
print("   Electricity Board")
print("-----------------------")   
input("Enter the EB NO:")
input("Enter the custamer name:")
precious=int(input("Reading for precious month:"))
current=int(input("Reading for current month:"))
total=precious-current
print("Total unit consumed:",total)
paid=total*5
print("Amount to be paid rs :",paid)
