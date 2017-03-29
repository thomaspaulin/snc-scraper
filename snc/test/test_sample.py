# a simple test to make travis pass while there is no code to be tested
def plus_one(x):
    return x + 1

def test_answer():
    assert plus_one(1) == 2
