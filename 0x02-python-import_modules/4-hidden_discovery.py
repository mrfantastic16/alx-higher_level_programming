#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4

    lst = []

    for names in hidden_4.__dict__:
        if not (names.startswith('__')):
            lst.append(names)

    lst.sort()

    for name in lst:
        print(name)
