from sentence_transformers import SentenceTransformer
from sentence_transformers.cross_encoder import CrossEncoder

model = SentenceTransformer("all-mpnet-base-v2")
encoderModel = CrossEncoder("cross-encoder/stsb-distilroberta-base")

sentence = "a man sitting at a table with a book and a cup. a woman sitting at a desk writing on a piece of paper. a woman sitting on a toilet with a cell in her hand. a woman sitting at a table with a laptop. a woman sitting at a table"

embedding = model.encode(sentence)
test = "I love this weather"
test2 = "I weather today lovely"
test3 = "I love playing games"
test4 = "Man and woman reading together"

testEmbed = model.encode(test)
testEmbed2 = model.encode(test2)
testEmbed3 = model.encode(test3)
testEmbed4 = model.encode(test4)

similarity = model.similarity(embedding, testEmbed)
print(similarity.item())
similarity = model.similarity(embedding, testEmbed2)
print(similarity.item())
similarity = model.similarity(embedding, testEmbed3)
print(similarity.item())
similarity = model.similarity(embedding, testEmbed4)
print(similarity.item())
