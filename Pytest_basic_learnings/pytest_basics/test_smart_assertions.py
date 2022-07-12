from  smart_assertions import soft_assert, verify_expectations

def test_something():
    soft_assert(1 == 2)
    soft_assert(2 < 1, 'Message if test failed')
    soft_assert('one' != 'two', 'Some message')
    verify_expectations()
