# Function to return score of matched words in the query sentence and array of sentences
def matching_words(sent1, sent2):
    words1 = sent1.split(" ")
    words2 = sent2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':
    sentences = ["Python is a good language", "Python is not a snake",
                 "Sarfaraz is a good boy", "Python is my new lover"]

    query = input("Please enter the query string\n")

    scores = [matching_words(query, sentence) for sentence in sentences]
    sorted_sent_score = [sent_score for sent_score in sorted(
        zip(scores, sentences), reverse=True)]
    print(f"{len(sorted_sent_score)} results found!")
    for score, item in sorted_sent_score:
        print(f"\"{item}\" with a score of {score}")
