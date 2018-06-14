from enemy import Enemy, Troll, Vampyre

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

vamp = Vampyre("Xen")
print(vamp)

vamp.take_damage(4)
print(vamp)
print("----Trying to kill Xen----")

while vamp._alive:
    vamp.take_damage(2)
    # print(vamp)

vamp._lives = 0
vamp._hit_points = 1
print(vamp)