import os 
import time

while True:
    os.system("cls")
    toy_type = (1,2,3)
    input_toy_type = int(input("what type of toy do you want to buy? 1. batery_based 2. key_based 3. electrical charging based "))
    if input_toy_type in toy_type:
        print("you have choosed a toy")
        non_discouted_price = int(input("what is the non discounted price of the toy? "))
        if input_toy_type == toy_type[0]:
            if non_discouted_price > 1000:
                discouted_price = non_discouted_price - (non_discouted_price * 0.1)
                print(f"product code = {toy_type[0]}")
                print(f"order price = {non_discouted_price}")
                print(f"discounted price = {discouted_price}")
            else:
                print(f"product code = {toy_type[0]}")
                print(f"order price = {non_discouted_price}")
        elif input_toy_type == toy_type[1]:   
            if non_discouted_price > 100:
                discouted_price = non_discouted_price - (non_discouted_price * 0.05)
                print(f"product code = {toy_type[1]}")
                print(f"order price = {non_discouted_price}")
                print(f"discounted price = {discouted_price}")
            else:
                print(f"product code = {toy_type[1]}")
                print(f"order price = {non_discouted_price}")
        elif input_toy_type == toy_type[2]:
            if non_discouted_price > 500:
                discouted_price = non_discouted_price - (non_discouted_price * 0.1)
                print(f"product code = {toy_type[2]}")
                print(f"order price = {non_discouted_price}")
                print(f"discounted price = {discouted_price}")
            else:
                print(f"product code = {toy_type[2]}")
                print(f"order price = {non_discouted_price}")
    else:
        print("invalid input, please choose a toy type between 1 and 3")
    time.sleep(5)
