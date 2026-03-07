import pytest
from root import root

@pytest.mark.parametrize(
        ("num", "num_root"),
        (
            (100,10),
            (81,9),
            (49,7),
            (36,6),
            (25,5),
                    )
)

def test_root(num, num_root):
    assert root(num) == num_root
