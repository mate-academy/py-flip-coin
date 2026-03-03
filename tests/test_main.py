from app.main import flip_coin

def test_flip_coin_distribution() -> None:
    results = flip_coin()
    total = sum(results.values())
    # Проверка, что сумма всех процентов примерно 100
    assert 99 <= total <= 101
    # Проверка ключей
    for k in range(11):
        assert k in results
