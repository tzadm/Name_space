calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string_):
    count_calls()
    tuple_1 = [len(str(string_)), str(string_).upper(), str(string_).lower()]
    tuple_1 = tuple(tuple_1)

    return tuple_1


def is_contains(string__, list_):
    count_calls()
    string__ = str(string__).upper()
    list_2 = []
    for i in list_:
        list_2.append(i.upper())
    if string__ in list_2:
        return True
    else:
        return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
