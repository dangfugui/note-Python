import pytest

def test_main():
    print "test_main"
    assert 5 != 5

def test_2():
    print "test_2"

if __name__ == '__main__':
    pytest.main()