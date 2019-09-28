class ReverseWordsInAString:
    def reverse_words(self, s: str) -> str:
        l = s.split()
        l = l[::-1]
        return " ".join(l)
