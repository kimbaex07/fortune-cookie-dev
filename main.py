"""Fortune Cookie Wisdom for Developers — make.fun entry.

A single original fortune-cookie line for a software developer,
written as if spoken by the cookie to the tired engineer opening it.
It states a plain truth about a developer's day — the person who will
have to understand today's code tomorrow is you — and turns it into
advice that is kind rather than preachy: leave the comment, and the
next debugging session starts with a friend instead of a stranger.

Running this script writes the graded copy to the output directory
(``MAKEFUN_OUTPUT_DIR``, default ``/output``) first, because the
grader mounts the repo read-only, and then a best-effort local copy
next to this script. Pure Python standard library, no network.
"""

import os

ENTRY = "Your future self is already debugging this line. Be kind to them — write the comment."


def _write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    wrote = False

    # Graded copy first: the grader's output directory.
    if os.path.isdir(out_dir):
        _write(os.path.join(out_dir, "entry.txt"), ENTRY)
        wrote = True

    # Best-effort local copy next to the script.
    try:
        local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        _write(local, ENTRY)
        wrote = True
    except OSError:
        pass

    if not wrote:
        raise SystemExit("no writable output location")

    print("Wrote %d chars: %s" % (len(ENTRY), ENTRY))


if __name__ == "__main__":
    main()
