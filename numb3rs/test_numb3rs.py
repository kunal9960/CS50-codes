from numb3rs import validate

def main():
    test_t()
    test_f()

def test_t():
    assert validate("123.123.123.123") == True
    assert validate("12.13.3.123") == True

def test_f():
    assert validate("1233.123.123.123") == False
    assert validate("1.555.555.555") == False
    assert validate("cat") == False

if __name__ == "__main__":
    main()
