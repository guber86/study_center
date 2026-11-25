from prepare_text import load_text # обращение к файлу колеги
def split_into_chunks(text):
    if not text or not text.strip():
        return []
    chunks = []
    sentences = text.split("\n")

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            chunks.append(sentence)
    return chunks
if __name__ == "__main__":
    result = split_into_chunks(load_text()) # изменения из-за файла колеги


    print("Количество чанков:", len(result))

    for number, chunk in enumerate(result, start=1):
        print(f"Чанк {number}: {chunk}")
    print("Последний чанк:", result[-1])
    print("Первый соседний чанк:", result[0])
    print("Второй соседний чанк:", result[1])