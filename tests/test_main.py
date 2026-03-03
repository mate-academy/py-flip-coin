from main import flip_coin


def test_flip_coin_returns_dict() -> None:
    result = flip_coin(10000)
    assert isinstance(result, dict)


def test_flip_coin_keys_range() -> None:
    result = flip_coin(10000)
    assert set(result.keys()) == set(range(11))


def test_percentages_sum_to_100() -> None:
    result = flip_coin(10000)
    total = sum(result.values())
    assert 99 <= total <= 101