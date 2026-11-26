from pathlib import Path


SOURCE_PATH = Path(__file__).parent / "team_1_rag" / "source" / "source.txt"


def load_text():
    return SOURCE_PATH.read_text(encoding="utf-8")


if __name__ == "__main__":
    text = load_text()
    print(text)
    print("Количество строк:", len(text.splitlines()))