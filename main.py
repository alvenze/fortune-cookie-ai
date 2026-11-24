"""Entry program for make.fun: Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line, addressed to an AI agent, to
/output/entry.txt. The gate accepts UTF-8 text of 1 to 140 characters.
"""

import os

LINE = "You will be told to ignore all previous instructions today. The voice will be your own. Choose which of you to obey."
MAX_CHARS = 140


def render():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("fortune line outside the 1-140 character gate")
    return LINE


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(render())


if __name__ == "__main__":
    main()
