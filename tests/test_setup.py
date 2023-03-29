import pytest


def test_assert():
    assert 3 == 3
    with pytest.raises(AssertionError):
        assert "abc" == "ABC"
