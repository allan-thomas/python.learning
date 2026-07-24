cart_count = 0

if cart_count !=2:
    # raise Exception("Cart count should be 2")
    pass

assert(cart_count == 0), "Cart count should be 2"

try:
    with open("teest.txt","r") as file:
        file.read()

except Exception as e:
    print("Exception occured while reading the file, as file is not there")
    print(e)

finally:
    print("This will be executed always, as im inside finally")