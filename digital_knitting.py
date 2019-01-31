
needle_size = 12

def row_maker(ridge_size, stich_type, ending):

    for i in range(ridge_size):
        print(stich_type, end = "")
    print("", end = ending)

def make_needles(ridge_size):
    for i in range(2):
        for i in range(ridge_size):
            print("-", end = "")
        print(" ", end = "")
    print("", end = "\n")

def make_digital_scarf(size):

    row_maker(20, "- ", ">\n")
    for i in range(size):
        if i % 2 == 0:
            row_maker(15, "X ", "\n")
        else:
            row_maker(15, " X", "\n")
    row_maker(20, "- ", ">\n")



print("\nHello, welcome to the Brinko Knitter 3002. Here is a step by step digital kniting guide.")
print("This is not a substanstive knitting tutorial, but more of a guide for newcomers.")


print("First: make a slipknot.")
print("\nS") # SLIPKNOT

print("\nSecond: attach it to a needle (don't make it too tight!)")

print("\nS")
make_needles(needle_size)


print("\nThen, make the ridge on the primary needle.\n")
row_maker(8, "R", "\n")
row_maker(10, "-", "\n")


print("\nThen, here's where you actually get to knit!")
print("Adjust both of your needles so the slipknot is at the bottokm of the needle,")
print("Begin to adjust the ridges downwards towards the end of the needle")

print("\nPut the other needle in the loop from the backwards side")
print("Put the yarn in between both of the needles and scoop the loop on the other needle.")
print("HOLY COW! That\'s it! It\'s midly challenging and awkward, but you can do it!\n")


row_maker(7, "R", "\n")
make_needles(needle_size)
for i in range(needle_size+1):
    print(" ", end = "")
print("X")



print("\nDo that for all of the other ridges.\n")

make_needles(needle_size)
for i in range(needle_size+1):
    print(" ", end = "")
row_maker(8, "X", "\n")

print("\nThat\'s the basics to knitting!")
print("\n How long (in lines) do you want your digitally created scarf to be?\n")

user_scarf_size = int(input())

make_digital_scarf(user_scarf_size)
