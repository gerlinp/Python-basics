def calculate_total(*args):
    total = sum(args)
    print(total)

# calculate_total(25,25,20,30)

def packer(*args):
    print("These are the characters I plan to try in SF6:")
    print(args)
    
packer("Kimberly", "DeeJay", "Marisa", "Jamie")