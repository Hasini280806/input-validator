from validator import is_valid_email, is_valid_phone, is_valid_age

def test_valid_email():
    assert is_valid_email("test@example.com")

def test_invalid_email():
    assert not is_valid_email("testexample.com")

def test_valid_phone():
    assert is_valid_phone("9876543210")

def test_invalid_phone():
    assert not is_valid_phone("98765")

def test_valid_age():
    assert is_valid_age("25")

def test_invalid_age():
    assert not is_valid_age("150")
