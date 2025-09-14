from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Optional, Pattern, Tuple


@dataclass(frozen=True)
class MatchResult:
    text: str
    span: Tuple[int, int]


class TextMemory:
    """A compact, deterministic memory abstraction enabling regex-based retrieval over supplied text corpora."""

    def __init__(self, initial_text: str = "") -> None:
        self._text = initial_text or ""

    @property
    def text(self) -> str:
        return self._text

    def set(self, text: str) -> None:
        self._text = text or ""

    def append(self, text: str, sep: str = "\n") -> None:
        if not text:
            return
        if self._text and not self._text.endswith(sep):
            self._text += sep
        self._text += text

    def clear(self) -> None:
        self._text = ""

    def search_matches(
        self,
        pattern: str | Pattern[str],
        *,
        flags: int = 0,
        limit: Optional[int] = None,
    ) -> List[MatchResult]:
        """Find regex matches and return match substrings with spans."""
        try:
            rx = re.compile(pattern, flags) if isinstance(pattern, str) else pattern
        except re.error as exc:
            raise ValueError(f"Invalid regex: {exc}") from exc

        results: List[MatchResult] = []
        for m in rx.finditer(self._text):
            s, e = m.span()
            results.append(MatchResult(text=self._text[s:e], span=(s, e)))
            if limit is not None and len(results) >= limit:
                break
        return results

    def search(self, pattern: str | Pattern[str], *, flags: int = 0, limit: Optional[int] = None) -> List[str]:
        """Convenience: return matched substrings only."""
        return [m.text for m in self.search_matches(pattern, flags=flags, limit=limit)]


__all__ = ["TextMemory", "MatchResult"]


