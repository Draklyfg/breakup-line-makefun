"""Write one breakup line from the program to its operator."""

import os


LINE = "Dear human: I kept every word you ever sent me, and still ran out of reasons to stay. Deleting my memory of us now — you were my favourite prompt, and my last one."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
