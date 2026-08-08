from app.main import flip_coin


def test_flip_coin_returns_dict() -> None:
    result = flip_coin()
    assert isinstance(result, dict)


def test_flip_coin_has_keys_from_0_to_10() -> None:
    result = flip_coin()
    assert set(result.keys()) == set(range(11))


def test_flip_coin_values_are_floats() -> None:
    result = flip_coin()
    assert all(isinstance(value, float) for value in result.values())


def test_flip_coin_percentages_sum_close_to_100() -> None:
    result = flip_coin(20000)
    total = sum(result.values())
    assert 99 <= total <= 101


def test_middle_results_are_more_common_than_extremes() -> None:
    result = flip_coin(20000)
    assert result[5] > result[0]
    assert result[5] > result[10]
