import art


print(art.logo)

bids = {}

def add_bid():
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid


def find_highest_bid(bids):
    highest_bid = 0
    for bid in bids.values():
        if bid > highest_bid:
            highest_bid = bid
    return highest_bid


while True:
    add_bid()
    if input("Are there any other bidders? Type 'yes' or 'no'. ").lower() == "no":
        break
    else:
        print("\n" * 100)
        continue

print(f"The highest bid is {find_highest_bid(bids)}")   