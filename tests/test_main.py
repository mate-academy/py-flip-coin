from app.main import flip_coin
from typing import Dict


def test_flip_coin_distribution() -> None:
    """Test that flip_coin returns a dict with 0-10 keys and percentages."""
    results: Dict[int, float] = flip_coin()
    # Проверяем все ключи от 0 до 10
    assert all(k in results for k in range(11))
    # Проверяем, что значения - числа от 0 до 100
    assert all(0 <= v <= 100 for v in results.values())
    # Проверяем, что сумма примерно 100%
    total = sum(results.values())
    assert 99.0 <= total <= 101.0
