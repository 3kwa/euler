def number_to_words(number):
    """
    >>> number_to_words(5)
    'five'
    >>> number_to_words(10)
    'ten'
    >>> number_to_words(11)
    'eleven'
    >>> number_to_words(20)
    'twenty'
    >>> number_to_words(21)
    'twenty one'
    >>> number_to_words(300)
    'three hundred'
    >>> number_to_words(315)
    'three hundred and fifteen'
    >>> number_to_words(1000)
    'one thousand'
    >>> number_to_words(2540)
    'two thousand five hundred and forty'
    >>> number_to_words(1013)
    'one thousand and thirteen'
    >>> number_to_words(1001)
    'one thousand and one'
    """
    string = str(number)
    if len(string) == 0:
        return

    digit = string[0]
    next_ = string[1:]

    if len(string) == 4:
        and_ = ' ' if next_[0] != '0' or int(next_) == 0 else ' and '
        return ''.join(
                ( digit_to_word(int(digit)),
                  'thousand',
                  and_,
                  number_to_words(int(next_)))
                ).strip()

    if len(string) == 3:
        and_ = '' if int(next_) == 0 else ' and '
        return ''.join(
                 ( digit_to_word(int(digit)),
                   'hundred',
                   and_,
                   number_to_words(int(next_)))
                 ).strip()

    if len(string) == 2:
        if string[0] == '1':
            return english(int(string))
        return ''.join(
                ( tens_to_word(int(digit)),
                  number_to_words(int(next_)) )
            ).strip()

    if len(string) == 1:
        return digit_to_word(number).strip()

def digit_to_word(digit):
    """
    >>> digit_to_word(1)
    'one '
    """
    ref = {
        0 : '',
        1 : 'one ',
        2 : 'two ',
        3 : 'three ',
        4 : 'four ',
        5 : 'five ',
        6 : 'six ',
        7 : 'seven ',
        8 : 'eight ',
        9 : 'nine ' }
    return ref[digit]

def tens_to_word(digit):
    """
    >>> tens_to_word(2)
    'twenty '
    """
    ref = {
        2 : 'twenty ',
        3 : 'thirty ',
        4 : 'forty ',
        5 : 'fifty ',
        6 : 'sixty ',
        7 : 'seventy ',
        8 : 'eighty ',
        9 : 'ninety ' }
    return ref[digit]

def english(digit):
    ref = {
        10 : 'ten',
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen',
        }
    return ref[digit]

def used_letters(number):
    """
    >>> used_letters(342)
    23
    >>> used_letters(115)
    20
    """
    return len(number_to_words(number).replace(' ', ''))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
    print sum(used_letters(i) for i in range(1,1001))
