import pytest
from app.main import flip_coin


def test_flip_coin_returns_dict() -> None:
    result = flip_coin()
    assert isinstance(result, dict)


def test_flip_coin_has_correct_keys() -> None:
    result = flip_coin()
    expected_keys = list(range(11))
    assert list(result.keys()) == expected_keys


def test_flip_coin_values_are_floats() -> None:
    result = flip_coin()
    for value in result.values():
        assert isinstance(value, (int, float))


def test_sum_of_percentages_is_about_100() -> None:
    result = flip_coin()
    total = sum(result.values())
    assert pytest.approx(total, abs=0.2) == 100


def test_gaussian_distribution_shape() -> None:
    result = flip_coin()
    assert result[5] > result[0]
    assert result[5] > result[10]
