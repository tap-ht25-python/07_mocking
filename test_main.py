from main import add, calculate

def test_add():
    # Arrange
    x = 12
    y = 3
    expected = 15

    # Act
    actual = add(x, y)

    # Assert
    assert actual == expected


def test_calculate():
    test_data = [10, 4, 5, 3]  # (10+4) - (5+3) -> 6
    expected = 6
    actual = calculate(test_data[0], test_data[1], test_data[2], test_data[3])
    assert actual == expected

