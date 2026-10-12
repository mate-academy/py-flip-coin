
from main import flip_coin


def test_returns_percentages_for_zero_to_ten_heads() -> None:
    result = flip_coin()

    assert set(result.keys()) == set(range(11))


def test_percentages_are_valid() -> None:
    result = flip_coin()

    assert all(0 <= percentage <= 100 for percentage in result.values())


def test_percentages_add_up_to_about_100() -> None:
    result = flip_coin()

    assert abs(sum(result.values()) - 100) < 0.2


def test_middle_results_are_more_likely_than_edges() -> None:
    result = flip_coin()

    assert result[5] > result[0]
    assert result[5] > result[10]
