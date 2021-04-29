#!/usr/bin/python3
if __name__ == "__main__":
    import sys
add = 0
for iter in sys.argv[1:]:
    add += int(iter)
print('{}'.format(add))
