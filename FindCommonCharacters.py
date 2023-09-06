class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
#Lista para armazenar os caracteres comuns
        common_chars = []
        
#Dicionário para a contagem mínima de cada caractere
        min_count = {}
        
#Contagem da primeira palavra
        for char in words[0]:
            min_count[char] = min_count.get(char, 0) + 1
        
#Palavras restantes
        for word in words[1:]:
#Dicionário para a contagem dos caracteres na palavra atual
            word_count = {}
#Contar a ocorrência de cada caractere na palavra atual
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1

#Atualizar o dicionário min_count com a contagem mínima de caracteres
            for char in min_count:
                if char in word_count:
                    min_count[char] = min(min_count[char], word_count[char])
                else:
                    min_count[char] = 0
        
#Lista de caracteres comuns com base na contagem mínima
        for char, count in min_count.items():
            common_chars.extend([char] * count)
        
        return common_chars