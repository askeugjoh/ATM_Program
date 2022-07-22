import time
ts = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", ts))

while True:

     print("\n**********Main Menu***********")
     print("1.  Display Orders")
     print("2.  Add New Order")
     print("3.  Remove Order")
     print("4.  Edit Order")
     print("5.  Save Order")
     print("6.  Exit Program")
     menu_option = input("Select an option:")

     if menu_option == "1":
         add = input("Enter new transaction:")
         print("Added")

     elif (menu_option == "2"):
         edit = input("Edit transaction:")
         print("Removed")

     elif (menu_option == "3"):
         old_amount = input("Enter the transaction key to edit:")
         new_amount = input("Enter the new transaction key:")

     elif (menu_option == "4"):
         print(f"**********Transaction*********** \n{new_amount}")



     elif menu_option == "5":
         exit()


         continue






















