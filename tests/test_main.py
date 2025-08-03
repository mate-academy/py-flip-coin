import pytest
import matplotlib.pyplot as plt
from unittest.mock import patch

from app.main import flip_coin, draw_gaussian_distribution_graph


def test_func_should_return_dict():
    assert isinstance(flip_coin(), dict), (
        "Function 'flip_coin' should return dictionary"
    )


def test_function_should_return_different_values():
    cache = set()

    for _ in range(20):
        coins = flip_coin()
        cache.add(tuple(result for result in coins.values()))

    assert len(cache) == 20, (
        "Function should return different values, "
        "because 'random' should be used"
    )


@pytest.mark.parametrize(
    "number, expected, limit",
    [
        pytest.param(
            5,
            22,
            27,
        ),
        pytest.param(
            4,
            18,
            22
        ),
        pytest.param(
            6,
            18,
            22
        ),
        pytest.param(
            3,
            10,
            18
        ),
        pytest.param(
            7,
            10,
            18
        ),
        pytest.param(
            2,
            2,
            10
        ),
        pytest.param(
            8,
            2,
            10
        ),
        pytest.param(
            1,
            0.6,
            2
        ),
        pytest.param(
            9,
            0.6,
            2
        ),
        pytest.param(
            10,
            0.01,
            0.6
        ),
        pytest.param(
            0,
            0.01,
            0.6
        ),
    ],
)
def test_gausian_distribution(number, expected, limit):
    for _ in range(20):
        coins = flip_coin()

        assert expected <= coins[number] <= limit, (
            f"There must be > {number}% of '{expected}' value"
        )


def test_draw_gaussian_distribution_graph():
    """Test that the graph function runs without errors."""
    with patch('matplotlib.pyplot.show') as mock_show:
        draw_gaussian_distribution_graph()
        mock_show.assert_called_once()


def test_draw_gaussian_distribution_graph_creates_plot():
    """Test that the graph function creates appropriate plot elements."""
    with patch('matplotlib.pyplot.show'):
        with patch('matplotlib.pyplot.bar') as mock_bar:
            with patch('matplotlib.pyplot.xlabel') as mock_xlabel:
                with patch('matplotlib.pyplot.ylabel') as mock_ylabel:
                    with patch('matplotlib.pyplot.title') as mock_title:
                        draw_gaussian_distribution_graph()
                        
                        mock_bar.assert_called_once()
                        mock_xlabel.assert_called_once_with('Number of Heads')
                        mock_ylabel.assert_called_once_with('Percentage (%)')
                        mock_title.assert_called_once_with('Gaussian Distribution of Coin Flip Results')
