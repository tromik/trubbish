def diamond(n):
    # import pdb; pdb.set_trace()
    # Make some diamonds!
    diamond = ""
    spaces = 0
    if not (n is None or n % 2 == 0):
        for i in range(1, n + 1, 2):
            spaces = (n - i)/2 * " "
            diamond += spaces + ("*" * i) + "\n"
        for i in range(n - 2, 0, -2):
            spaces = (n - i)/2 * " "
            diamond += spaces + ("*" * i) + "\n"
        if 
        return diamond
    else:
        return None


print diamond("")
