import pygame

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Minha Tela do Pygame")

largura_parte = largura_tela
altura_parte = altura_tela // 2

rodando = True
while rodando:
    # Lidar com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Atualizar a lógica do jogo
    
    # Renderizar a tela
    tela.fill((0, 0, 0))  # Preenche a tela com a cor preta (RGB: 0, 0, 0)

    # Desenha as duas partes da tela
    parte_superior = pygame.Rect(0, 0, largura_parte, altura_parte)
    parte_inferior = pygame.Rect(largura_parte, 0, largura_parte, altura_parte)
    pygame.draw.rect(tela, (255, 0, 0), parte_superior)  # Desenha a parte esquerda em vermelho
    pygame.draw.rect(tela, (0, 0, 255), parte_inferior)  # Desenha a parte direita em azul

    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
