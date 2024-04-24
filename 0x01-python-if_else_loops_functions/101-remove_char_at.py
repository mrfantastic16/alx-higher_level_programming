def remove_char_at(str, n):
    new_s = []

    for i in range(len(str)):
        if i == n:
            continue
        new_s.append(str[i])

    return "".join(new_s)
