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

test_text = "Курс «Основы Пайтона» длится восемь недель.\nЗанятия курса «Основы Пайтона» проходят по понедельникам и средам с 18:00 до 20:00.\nМесяц обучения на курсе «Основы Пайтона» стоит 48000 драмов."

result = split_into_chunks(test_text)

print("Количество чанков:", len(result))

for number, chunk in enumerate(result, start=1):
    print(f"Чанк {number}: {chunk}")
print("Последний чанк:", result[-1])
print("Первый соседний чанк:", result[0])
print("Второй соседний чанк:", result[1])