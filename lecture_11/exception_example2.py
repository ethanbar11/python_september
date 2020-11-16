try:
    lst = [1, 2, 3]
    print(lst[5])
    # print('x is :', x)
except ZeroDivisionError as e:
    print(e)
    print('There was a zero division error!')
except IndexError as e:
    print('e is:',e)
    print('There was an index error!')
except Exception as e:
    # print()
    print('There was a problem!')
except:
    print('hello')
