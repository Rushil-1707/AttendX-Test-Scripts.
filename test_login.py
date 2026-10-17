
def login(username, password):
    if username == "student" and password == "1234":
        return "Login Successful"
    return "Invalid Credentials"


def test_valid_login():
    assert login("student", "1234") == "Login Successful"


def test_invalid_login():
    assert login("student", "wrong") == "Invalid Credentials"


def test_empty_login():
    assert login("", "") == "Invalid Credentials"
