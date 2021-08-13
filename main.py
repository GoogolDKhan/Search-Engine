def matchingWords(sent1, sent2):
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

    scores = [matchingWords(query, sentence) for sentence in sentences]
    sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences), reverse=True)]
    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f"\"{item}\" with a score of {score}")
