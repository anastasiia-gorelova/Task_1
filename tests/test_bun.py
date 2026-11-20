from praktikum.bun import Bun


def test_bun_returns_its_name_and_price():
    bun = Bun('brioche', 12.5)

    assert (bun.get_name(), bun.get_price()) == ('brioche', 12.5)
