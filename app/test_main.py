import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(0, [0, 0, 0,0], id="zero cents"),
        pytest.param(4, [4, 0, 0, 0], id="only pennies"),
        pytest.param(5, [0, 1, 0, 0], id="1 nickel"),
        pytest.param(10, [0, 0, 1, 0], id="1 dime"),
        pytest.param(25, [0, 0 ,0, 1], id="1 quarters"),
        pytest.param(50, [0, 0, 0, 2], id="boundary 50"),
        pytest.param(68, [3, 1, 1, 2], id="multiple quarters")

    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected

# Еквівалентні класи — це групи вхідних значень,
# для яких програма працює однаково і повертає
# однаковий результат. Тому для тестування
# достатньо перевірити одне представницьке
# значення з кожної такої групи.
#
# Еквівалентні класи для get_coin_combination:
# 0
# 1–4
# 5–9
# 10–24
# 25–49
# ≥ 50
