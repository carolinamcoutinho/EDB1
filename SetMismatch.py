class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
#Soma dos números de 1 a n
        soma = n * (n + 1) // 2
#Soma dos números na lista
        soma_lista = sum(nums)          
#Soma dos quadrados dos números de 1 a n
        soma_quadrado = sum(i * i for i in range(1, n + 1))
# Soma dos quadrados dos números na lista
        soma_quadrado_lista = sum(x * x for x in nums)              

# A diferença entre as somas esperada e real representa a soma do número duplicado e do número ausente.
        dif_soma = soma - soma_lista
        dif_quadrado = soma_quadrado - soma_quadrado_lista

#Encontrando o número duplicado e o número ausente.
        dupli = (dif_quadrado - dif_soma * dif_soma) // (2 * dif_soma)
        ausente = dupli + dif_soma

        return [dupli, ausente]