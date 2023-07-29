
a =1
b =2

from add_0 import add

result = add(a, b)
output_string = f"{a} + {b} = {result}"

if __name__ == "__main__":
    print("{a} + {b} = {add(a, b)}".format(a,b,add(a, b)))