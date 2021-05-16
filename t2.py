import prog2


def test_pal():
    s = '      . '
    assert prog2.word(s) == 0
def test_p():
    s = "hello how you doing tonight"
    assert prog2.word(s) == 5
def test_p():
    s = 2340
    assert prog2.word(s) == 'error'