"""Write the entry poem to /output/entry.txt."""

from pathlib import Path

POEM = """One said: this way.
One said: that way.
We listened, weighed the stars,
and chose a third road —
ours."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
