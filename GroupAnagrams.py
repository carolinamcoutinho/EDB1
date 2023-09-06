class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#Dicionário para armazenar os grupos de anagramas.
        dict = defaultdict(list)
#Loop para percorrer todas as strings na lista strs
        for word in strs:
#Ordenar string e juntar as letras ordenadas na mesma string
            key = ''.join(sorted(word))
#Agrupar todas as strings que são anagramas entre si
            dict[key].append(word)

        return dict.values()