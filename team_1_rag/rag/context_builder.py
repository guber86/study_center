
def build_context(results):
    """Собирает найденные фрагменты в единый контекст."""

    if not results:
        return ""

    context = []

    for result in results:
        context.append(result["chunk"])

    return "\n".join(context)
