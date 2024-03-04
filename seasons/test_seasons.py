from seasons import minutes_lived

def main():
    test_1()
    test_2()

def test_1():
    assert minutes_lived(2002, 10, 26) == "Eleven million, two hundred thirty thousand, five hundred sixty minutes"
    assert minutes_lived(2000, 2, 1) == "Twelve million, six hundred sixty-seven thousand, six hundred eighty minutes"

def test_2():
    assert minutes_lived(23, 1, 2000) == "Invalid Date"

if __name__ == "__main__":
    main()
