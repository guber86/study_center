from sentence_transformers import SentenceTransformer


MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"


def load_model():
    """Загружает модель для создания эмбеддингов."""
    return SentenceTransformer(MODEL_NAME)
