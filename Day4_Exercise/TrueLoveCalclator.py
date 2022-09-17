your_name = input("Please provide your name")

your_gf_name = input("Please provide your crush name")

full_name = your_name + your_gf_name

t = full_name.lower().count('t')
r = full_name.lower().count('r')
u = full_name.lower().count('u')
e =  full_name.lower().count('e')

l = full_name.lower().count('e')
o = full_name.lower().count('o')
v = full_name.lower().count('v')
e =  full_name.lower().count('e')

total_percent = str(t+r+u+e) + str(l+o+v+e)

print(f"Your total percent is {total_percent}")
