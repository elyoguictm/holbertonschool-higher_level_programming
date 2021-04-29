#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
for iter in dir(hidden_4):
    if iter[1] != '_':
        print(iter)
