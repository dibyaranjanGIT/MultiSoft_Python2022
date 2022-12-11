sum = 0
while (True):
    defaulter_name = input("Enter the name of the defaulter :")
    item_name = input("Enter the item name :")
    item_price = int(input("Enter the item price :"))

    try:
        with open("defaulters.txt", mode='a') as f:
            f.write(f"Defaulter Name: '{defaulter_name}' \n Item: {item_name} \t Price:{item_price}\n")
        user_continue = input("Press q to quit else press <-| to continue")
        if user_continue != 'q':
            continue
        else:
            print("Thank you for using !!")
            break
    except FileNotFoundError:
        with open("defaulters.txt", mode='w') as f:
            f.write(f"Defaulter Name '{defaulter_name}' ")

