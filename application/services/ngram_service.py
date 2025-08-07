from collections import Counter
import time

class NGramService:

    def get_ngrams(self, word, n):

        result = []

        for i in range(len(word) - n + 1):            
            result.append(word[i:i+n])

        ngrams_count = Counter(result)

        result = [ngram for ngram, count in ngrams_count.items() if count == 1]

        return set(result)

    def n_gram(self, word1, word2, n):

        ngrams1 = self.get_ngrams(word1, n)
        ngrams2 = self.get_ngrams(word2, n)

        intersection = ngrams1 & ngrams2

        A = len(ngrams1)
        B = len(ngrams2)
        C = len(intersection)

        if A + B == 0:
            return round(0,2)

        S = 2 * C / (A + B)

        return round(S, 2)

    def get_top_5(self, typed_word, n):

        result = []

        start_time = time.time()

        with open('pt-BR.txt', encoding='utf-8') as f:
            lexicons = [line.strip() for line in f if line.strip()]

        result = [{"word": word, "similarity": self.n_gram(typed_word, word, n)} for word in lexicons]

        result_sorted = sorted(result, key=lambda x: x["similarity"], reverse=True)

        stop_time = time.time()

        elapsed_time = stop_time - start_time
        print(f"Tempo de execução: {elapsed_time:.4f} segundos")

        top_n = 5
        print(f"\nTop {top_n} palavras mais semelhantes a '{typed_word}':")
        top_5_similarities = []

        for i in range(top_n):
            w = result_sorted[i]
            print(f"{i+1}. {w['word']} (similaridade: {w['similarity']})")
            top_5_similarities.append(result_sorted[i])

        return top_5_similarities

            