

croissant = 39
baguette = 278
discount = -50
valCroissant = int(input("Hoeveel croissantjes wilt u: "))
valBaguette = int(input("Hoeveel Baguettes wilt u: "))
valDiscount = int(input("Hoeveel kortingsbonnen heeft u: "))
myOrder ="De feestlunch kost je bij de bakker {} euro voor de {} croissantjes en de {} stokbroden als de {} kortingsbonnen nog geldig zijn!"

TOTAL = valCroissant*croissant+valBaguette*baguette+valDiscount*discount

print(myOrder.format(TOTAL/100, valCroissant, valBaguette, valDiscount))