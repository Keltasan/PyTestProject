import pytest
from src.main import palindrom_check

@pytest.mark.skip
@pytest.mark.mymark
def test_palindrom_check():
    assert palindrom_check(1111) == True

@pytest.mark.xfail
def test_palindrom_check2():
    assert palindrom_check(123454321) == True

@pytest.mark.xfail
@pytest.mark.mymark
def test_palindrom_check_false():
    assert palindrom_check(123465432) == True