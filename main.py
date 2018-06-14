from enemy import Enemy, Troll

ugly_troll = Troll("Pug")

print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

ugly_troll.take_damage(5)
another_troll.take_damage(3)
brother.take_damage(2)

print("{}\n{}\n{}".format(ugly_troll, another_troll, brother))
