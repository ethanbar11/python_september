for i in range(9):
    asterisk_line = ''
    asterisk_amount = 0
    if i <= 4:
        asterisk_amount = i + 1
    else:
        asterisk_amount = 9 - i
    for i in range(asterisk_amount):
        asterisk_line = asterisk_line + '*'
    print(asterisk_line)
