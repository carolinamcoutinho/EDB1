class Solution:
    def hIndex(self, citations: List[int]) -> int:
#Armazenar o comprimento da lista citations(quantos artigos foram publicados)
        artigos = len(citations)
#Variáveis para contagem
        ac = 0
        count = [0] * (artigos+1)
#Contar quantos artigos têm pelo menos 'citacao' citações, mas não mais do que n citações.
        for citacao in citations:
            count[min(citacao, artigos)] += 1
#Percorrer a lista e fazer contagem de artigos com citações
        for i, c in reversed(list(enumerate(count))):
            ac += c
            if ac >= i:
                return i