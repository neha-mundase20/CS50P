# from calculator import square

# def main():
#     test_square()

# def test_square():
#     try :
#         assert square(1)==1
#     except AssertionError:
#         print("That's an assertion error, 1 square is not 1 !")
#     try :
#             assert square(2)==4
#     except AssertionError:
#         print("That's an assertion error, 2 square is not 4 !")
#     try :
#             assert square(3)==9
#     except AssertionError:
#         print("That's an assertion error, 3 square is not 9 !")
#     try :
#             assert square(4)==16
#     except AssertionError:
#         print("That's an assertion error, 4 square is not 16 !")
#     finally:
#         print("Completed executing test_square function.")

# if __name__=="__main__":
#     main()

from calculator import square
import pytest

# def main():
#     test_square()

# def test_square():
#     assert square(1)==1
#     assert square(2)==4
#     assert square(3)==9
#     assert square(4)==16

# if __name__=="__main__":
#     main()

def main():
    test_positive()
    test_negative()
    test_zero()

def test_positive():
    assert square(1)==1
    assert square(2)==4
    assert square(3)==9
    assert square(4)==16

def test_negative():
    assert square(-1)==1
    assert square(-2)==4
    assert square(-3)==9
    assert square(-4)==16

def test_zero():
    assert square(0)==0

def test_str():
    with pytest.raises(TypeError):
        square("Neha")
    

if __name__=="__main__":
    main()