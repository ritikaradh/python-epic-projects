from replit import clear
auction_database = {}

def auction():
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  auction_database[name] = bid

auction()

base_case = 0
while(base_case == 0):
  need_to_clear = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if need_to_clear == "no":
    base_case = 1
    continue
  clear()
  auction()
  
highest_bid = 0
highest_bidder = ""
for key, value in auction_database.items():
  if value > highest_bid:
    highest_bidder = key
    highest_bid = value
clear()
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

##bug alert
#try to import os package and then utilise some of it command to clear the termina
#of clear() command.