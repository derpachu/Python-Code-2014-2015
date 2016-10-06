import drinks

coke = drinks.CocaCola()
print(coke)
coke.price_change(2)
print(coke)
coke.print_price_sticker()

WMilk = drinks.WhiteMilk(1)
print(WMilk)
WMilk.price_change(2)
print(WMilk)
WMilk.fat_perc_change(2)
print(WMilk)
WMilk.print_price_sticker()

CMilk = drinks.ChocolateMilk(1)
print(CMilk)
CMilk.price_change(2)
print(CMilk)
CMilk.fat_perc_change(2)
print(CMilk)
CMilk.print_price_sticker()
