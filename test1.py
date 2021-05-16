import prog1


def test_pal():
    s = 'whereerehw'
    assert prog1.p(s) == "not palindrome"
def test_p():
    s = "redder"
    assert prog1.p(s) == 'It is a palindrome'
def test_p():
    s = 2340
    assert prog1.p(s) == 'error'