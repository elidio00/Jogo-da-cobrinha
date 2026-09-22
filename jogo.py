import pygame
import random

pygame.init()

# Tamanho da tela
LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

relogio = pygame.time.Clock()

# Cores
VERDE = (0, 180, 0)     
AZUL = (0, 80, 255)     
AZUL_ESCURO = (0, 46, 180)
VERMELHO = (255, 0, 0)  
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
TAMANHO = 20

fonte = pygame.font.SysFont("Arial", 30)
fonte_grande = pygame.font.SysFont("Arial", 60)


def iniciar_jogo():

    cobra = [
        [400, 300],
        [380, 300],
        [360, 300]
    ]

    direcao = "DIREITA"

    comida_x = random.randrange(
        0, LARGURA - TAMANHO, TAMANHO
    )

    comida_y = random.randrange(
        0, ALTURA - TAMANHO, TAMANHO
    )

    pontos = 0
    perdeu = False

    return cobra, direcao, comida_x, comida_y, pontos, perdeu


cobra, direcao, comida_x, comida_y, pontos, perdeu = iniciar_jogo()

rodando = True

while rodando:

  
    # Evento

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:
                rodando = False

            # Cima
            if evento.key == pygame.K_UP and direcao != "BAIXO":
                direcao = "CIMA"

            # Baixo
            if evento.key == pygame.K_DOWN and direcao != "CIMA":
                direcao = "BAIXO"

            # Esquerda
            if evento.key == pygame.K_LEFT and direcao != "DIREITA":
                direcao = "ESQUERDA"

            # Direita
            if evento.key == pygame.K_RIGHT and direcao != "ESQUERDA":
                direcao = "DIREITA"

            # Reiniciar
            if evento.key == pygame.K_r and perdeu:
                cobra, direcao, comida_x, comida_y, pontos, perdeu = iniciar_jogo()


    # Movimento

    if not perdeu:

        cabeca = cobra[0].copy()

        if direcao == "CIMA":
            cabeca[1] -= TAMANHO

        if direcao == "BAIXO":
            cabeca[1] += TAMANHO

        if direcao == "ESQUERDA":
            cabeca[0] -= TAMANHO

        if direcao == "DIREITA":
            cabeca[0] += TAMANHO

        # Adiciona a nova cabeça
        cobra.insert(0, cabeca)

        # Comer Comida


        if cabeca[0] == comida_x and cabeca[1] == comida_y:

            pontos += 1

            comida_x = random.randrange(
                0, LARGURA - TAMANHO, TAMANHO
            )

            comida_y = random.randrange(
                0, ALTURA - TAMANHO, TAMANHO
            )

        else:
            # Remove o último pedaço
            cobra.pop()

        # Colisão com a parede

        if (
            cabeca[0] < 0
            or cabeca[0] >= LARGURA
            or cabeca[1] < 0
            or cabeca[1] >= ALTURA
        ):
            perdeu = True

        # =========================
        # COLISÃO COM O PRÓPRIO CORPO
        # =========================

        if cabeca in cobra[1:]:
            perdeu = True


#Desenhar o jogo

    # Fundo verde
    tela.fill(VERDE)

    # Desenhar cobra
    for parte in cobra:

        pygame.draw.rect(
            tela,
            AZUL,
            (
                parte[0],
                parte[1],
                TAMANHO,
                TAMANHO
            )
        )

    # Cabeça da cobra
    pygame.draw.rect(
        tela,
        AZUL_ESCURO,
        (
            cobra[0][0],
            cobra[0][1],
            TAMANHO,
            TAMANHO
        )
    )

#Desenhar a cobra

    pygame.draw.rect(
        tela,
        VERMELHO,
        (
            comida_x,
            comida_y,
            TAMANHO,
            TAMANHO
        )
    )

    # PONTUAÇÃO

    texto_pontos = fonte.render(
        "Pontos: " + str(pontos),
        True,
        BRANCO
    )

    tela.blit(
        texto_pontos,
        (20, 20)
    )

    # GAME OVER

    if perdeu:

        texto = fonte_grande.render(
            "GAME OVER",
            True,
            BRANCO
        )

        tela.blit(
            texto,
            (280, 240)
        )

        texto_reiniciar = fonte.render(
            "Pressione R para jogar novamente",
            True,
            BRANCO
        )

        tela.blit(
            texto_reiniciar,
            (230, 320)
        )

    # Atualiza a tela
    pygame.display.update()

    # Velocidade
    relogio.tick(10)

pygame.quit()