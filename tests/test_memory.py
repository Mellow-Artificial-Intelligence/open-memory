import re

from open_memory import TextMemory


def test_search_matches_basic():
    mem = TextMemory("alpha beta gamma\nAlpha BETA\n")
    matches = mem.search_matches(r"beta", flags=re.IGNORECASE)
    assert [m.text for m in matches] == ["beta", "BETA"]
    # spans are increasing and within bounds
    assert all(0 <= s < e for (s, e) in [m.span for m in matches])


def test_search_limit():
    mem = TextMemory("a a a a")
    matches = mem.search_matches(r"a", limit=2)
    assert len(matches) == 2


def test_search_exact_no_flags():
    mem = TextMemory("Foo foo")
    matches = mem.search_matches(r"foo")
    assert [m.text for m in matches] == ["foo"]
