from src.constants import KEYS_TO_SKIP


def embed_text_from_resume(resume_data, tokenizer, model):
    embedded_data = {}
    for key, words in resume_data.items():
        if key in KEYS_TO_SKIP:
            embedded_data[key] = words
        else:
            text = ' '.join(words)

            inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
            outputs = model(**inputs)

            cls_embeddings = outputs.last_hidden_state[:, 0, :].detach().numpy()
            embedded_data[key] = cls_embeddings[0].tolist()

    return embedded_data


def embed_corpus(corpus, tokenizer, model):
    embedded_corpus = []
    for document in corpus:
        inputs = tokenizer(document, return_tensors='pt', truncation=True, padding=True, max_length=512)
        outputs = model(**inputs)

        cls_embeddings = outputs.last_hidden_state[:, 0, :].detach().numpy()
        embedded_corpus.append(cls_embeddings[0].tolist())

    return embedded_corpus
