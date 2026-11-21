import pytest
import math
from gameplay import quest_progress as mod

CASES = [
    ("share", 'm.share(30, 100) == approx(0.3)'),
    ("progress", 'm.progress(50, 100, 10) == 5'),
    ("owner", 'm.owner("", "B") == "B"'),
    ("reset", 'm.reset_time(10, 8) == 18'),
    ("chain", 'm.chain_ok([True, True]) is True'),
    ("dedupe", 'm.dedupe("e", {"e"}) is False'),
    ("rollback", 'm.rollback(3, 5) == 0'),
    ("ordered", 'm.ordered([ (2, 0), (1, 0) ]) == [(1, 0), (2, 0)]'),
    ("ui", 'm.ui(7) == 7'),
    ("reward", 'm.reward(10, 2) == 12'),
    ("complete", 'm.complete(5, 5) is True'),
    ("clamp", 'm.clamp(12, 10) == 10'),
    ("key", 'm.quest_key("c1", 2) == "c1:2"'),
    ("daily", 'm.daily(100, 24) == 4'),
    ("id", 'm.progress_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
