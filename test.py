def my_function(a, b):
    return a+b


def test_my_function():
    assert my_function("hello", " world!") == "hello world!"