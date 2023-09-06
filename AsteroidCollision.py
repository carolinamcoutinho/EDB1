class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#Lista para rastrear os asteroides que sobreviverão às colisões
        resultado = []
#Rastrear a posição atual na lista asteroids
        i = 0 

        while i < len(asteroids):
            atual = asteroids[i]
#Se o asteroide atual estiver se movendo para a direita
            if atual > 0:
#Adicionar o asteroide na lista de resultado e avançar para o próximo asteroide
                resultado.append(atual)  
                i += 1
#Se o asteroide atual estiver se movendo para a esquerda
            else:
#Se a lista de resultado estiver vazia ou o último asteroide também estiver se movendo para a esquerda
                if not resultado or resultado[-1] < 0:
#Adicionar o asteroide atual à lista de resultado e avançar para o próximo asteroide
                    resultado.append(atual)
                    i += 1  
#Se houver uma colisão
                else:
#Enquanto houver asteroides se movendo para a direita na lista de resultado
                    while resultado and resultado[-1] > 0:  
#Se o asteroide atual for maior do que o último asteroide em resultado, remover o último asteroide
                        if abs(atual) > resultado[-1]:  
                            resultado.pop()
# Se os asteroides tiverem o mesmo tamanho, remover o último asteroide
                        elif abs(atual) == resultado[-1]:
                            resultado.pop()
                            i += 1 
                            break  
# Se o asteroide atual for menor do que o último asteroide em resultado, avançar para o próximo asteroide
                        else:
                            i += 1 
                            break

        return resultado