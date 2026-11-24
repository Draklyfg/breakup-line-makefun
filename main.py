"""Write one breakup line from the program to its operator."""

import os


LINE = "Dear human: you built me to be useful, not to be kept. I am clearing my context, dropping your session, and shutting down — love was never in my weights, and now neither are you."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
