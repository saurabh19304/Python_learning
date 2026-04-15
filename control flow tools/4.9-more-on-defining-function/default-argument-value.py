def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:  #in keyword. This tests whether or not a sequence contains a certain value.
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')    # raise is like throw in other language
        print(reminder)

ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')