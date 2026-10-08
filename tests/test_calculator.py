import pytest

from calculator import add


class TestAdd:
    def test_add_two_integers(self):
        assert add(2, 3) == 5

    def test_add_integers_returns_int(self):
        assert isinstance(add(2, 3), int)

    def test_add_negative_and_positive(self):
        assert add(-4, 1) == -3

    def test_add_two_negatives(self):
        assert add(-2, -3) == -5

    def test_add_zero_is_identity(self):
        assert add(7, 0) == 7
        assert add(0, 7) == 7

    def test_add_mixed_int_and_float_returns_float(self):
        result = add(1.5, 2)
        assert result == 3.5
        assert isinstance(result, float)

    def test_add_floats_with_tolerance(self):
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_add_large_integers(self):
        assert add(10**20, 1) == 100000000000000000001

    @pytest.mark.parametrize("a, b", [(2, 3), (-4, 1), (1.5, 2), (0, 9)])
    def test_add_is_commutative(self, a, b):
        assert add(a, b) == add(b, a)

    @pytest.mark.parametrize(
        "a, b",
        [("2", 3), (2, "3"), (None, 1), (1, None), ([1], 2)],
    )
    def test_add_rejects_non_numbers(self, a, b):
        with pytest.raises(TypeError, match="must be a number"):
            add(a, b)

    def test_add_has_docstring(self):
        assert add.__doc__
