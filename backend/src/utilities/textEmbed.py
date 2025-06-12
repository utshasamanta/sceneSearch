from sentence_transformers import SentenceTransformer
from sentence_transformers.cross_encoder import CrossEncoder

model = SentenceTransformer("all-mpnet-base-v2")
encoderModel = CrossEncoder("cross-encoder/stsb-distilroberta-base")

sentence = "The weather is lovely today"

embedding = model.encode(sentence)
test = "I love this weather"
testEmbed = model.encode(test)

similarity = model.similarity(embedding, testEmbed)
print(similarity.item())
