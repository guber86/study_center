from prompt_builder import build_prompt
from context_builder import build_context
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

from embeddings import load_model, create_embeddings
from vector_store import load_index


# def search_chunks(query, model, chunks, embeddings, top_k=3):
def search_chunks(query, model, chunks, embeddings, top_k=3, threshold=0.35):
    """Находит наиболее подходящие чанки по смыслу вопроса."""

    query_embedding = create_embeddings([query], model)

    scores = cosine_similarity(query_embedding, embeddings)[0]

    best_indices = scores.argsort()[::-1][:top_k]

    results = []

    for index in best_indices:
        score = float(scores[index])

        if score >= threshold:
            results.append({
                "chunk": chunks[index],
                "score": score
            })

    return results


if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parents[1]
    index_dir = project_dir / "index"

    # Загружаем сохранённую базу знаний
    chunks, embeddings = load_index(index_dir)

    # Загружаем модель
    model = load_model()

    # Проверяем поиск
    query = "Сколько стоит обучение Python?"
    # query = "Когда проходят занятия по курсу Python?"
    # query = "С какого возраста принимают студентов?"
    # query = "Сколько студентов может быть в одной группе?"
    # query = "Есть ли в центре обучение немецкому языку?"

    results = search_chunks(query, model, chunks, embeddings)

    print("Вопрос:", query)
    print("\nНайденные фрагменты:")

    if not results:
        print("В базе знаний нет подтверждённой информации.")
    else:
        for number, result in enumerate(results, start=1):
            print(f"\n{number}. Оценка: {result['score']:.4f}")
            print(result["chunk"])

        # Формируем контекст один раз после цикла
        context = build_context(results)

        print("\nСформированный контекст:")
        print(context if context else "Контекст отсутствует.")

        # Формируем промпт для языковой модели
        prompt = build_prompt(query, context)

        print("\nСформированный промпт:")
        print(prompt)