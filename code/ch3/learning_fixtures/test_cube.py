def test_cube():
    num = 42
    cube = num ** 3
    expected = num**2 * num
    assert cube == expected
