#\x72\x75\x64\x73\x6f\x6e\x20\x6d\x61\x72\x74\x69\x6e\x61
#Pizza calculator

#Customers can here choose the size and amount of pizza's
small_pizza = int(input("how much small pizza's do u want(25cm): "))
medium_pizza = int(input("how much medium pizza's do u want(30cm): "))
large_pizza = int(input("how much large pizza's do u want(35cm): "))

#Prizes per pizza
small_price = 5.50
medium_price = 8.25
large_price = 10.85

#Here python calculates the input of all the assigned variables
total_small = small_pizza  * small_price
total_medium = medium_pizza * medium_price
total_large = large_pizza  * large_price
final_total = total_small + total_medium + total_large
order = "You order {} small pizza's cost : ${}\nYou order {} medium pizza's cost : ${}\nYou order {} large pizza's cost : ${}\nyour total is ${}"
 

print(order.format(small_pizza, total_small, medium_pizza, total_medium, large_pizza, total_large, final_total))