from sentence_transformers import SentenceTransformer


MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"

model = SentenceTransformer(MODEL_NAME)


def get_vector(text):
    return model.encode(text, convert_to_numpy=True)


def get_vectors(chunks):
    result = []

    for chunk in chunks:
        vector = get_vector(chunk)
        result.append([vector, chunk])

    return result