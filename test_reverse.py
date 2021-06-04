import reverse

def testdefault():
    values = ("My name is V Tadimeti")
    val = reverse.reverse(values)
    assert val == "Tadimeti V is name My"

def testdefaultwithperiod():
    values = ("My name is V Tadimeti.")
    val = reverse.reverse(values)
    assert val == "Tadimeti V is name My."

def testwithnum():
    values = ("baMbmaB testing with numbers 1 2 3 34")
    val = reverse.reverse(values)
    assert val == "34 3 2 1 numbers with testing baMbmaB"
