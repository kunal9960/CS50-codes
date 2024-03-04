from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("theitshed") == "thtshd"
    assert shorten("THEITSHED") == "THTSHD"
    assert shorten("ThEiTsHed") == "ThTsHd"
    assert shorten("123456") == "123456"
    assert shorten("!£$%") == "!£$%"

if __name__ == "__main__":
    main()
    