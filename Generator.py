def gen(n):
    for i in range(n):
        yield i

print(gen(10))

def gen1(n):
    for i in range(n):
        return i

print(gen1(10))

# Generator generates the value on the fly , so that it does not take up spaces at the begining
# but it has the capability to generate it on the fly.  
