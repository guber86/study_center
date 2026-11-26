from pathlib import Path


BASE = Path(__file__).resolve().parents[2]


def get_database_path():
    return BASE / "database" / "database.txt"


def save(vectors):
    path = get_database_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        for vector, text in vectors:
            vector_str = " ".join(map(str, vector))
            file.write(f"{vector_str};{text}\n")