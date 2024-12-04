import pygame
import math

# Inicializar o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Trajetória de Bala")

# Cores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Definir pontos de origem e destino (jogador e inimigo)
origin = (100, 500)  # Posição do jogador (início)
target = (400, 300)  # Posição inicial do inimigo (alvo)

# Constantes físicas
gravity = -0.5  # Aceleração devido à gravidade (ajustável)
initial_velocity = 20  # Velocidade inicial da bala (ajustável)

# Função para calcular a trajetória com base na gravidade
def calculate_trajectory():
    points = []
    
    # Posições iniciais
    x0, y0 = origin
    target_x, target_y = target
    
    # Calcular a distância horizontal e vertical entre a origem e o alvo
    delta_x = target_x - x0
    delta_y = target_y - y0

    # Calcular o tempo necessário para alcançar o alvo na direção horizontal
    total_time = delta_x / initial_velocity
    
    # Calcular a velocidade inicial na direção vertical
    # Usando a equação: y = y0 + vy * t - 0.5 * g * t^2
    # Resolvendo para vy com base em y (distância vertical)
    vy_initial = (delta_y + 0.5 * gravity * total_time**2) / total_time
    
    # Número de passos para a simulação baseado na distância horizontal
    num_steps = max(int(delta_x / 2), 100)  # Aumentar o número de pontos proporcionalmente à distância
    time_step = total_time / num_steps  # Ajustar o passo de tempo

    # Trajetória
    for step in range(num_steps):
        t = step * time_step
        x = x0 + initial_velocity * t  # Movimento horizontal com velocidade constante
        y = y0 + vy_initial * t - 0.5 * gravity * t**2  # Movimento vertical com gravidade
        points.append((x, y))
        
        # Se a bala ultrapassar o inimigo, interrompe a trajetória
        if x >= target_x:
            break
    
    return points

# Função para desenhar a trajetória da bala
def draw_trajectory():
    points = calculate_trajectory()

    # Desenhar a trajetória da bala
    for i in range(len(points)-1):
        pygame.draw.line(screen, GREEN, points[i], points[i+1], 2)

# Função para desenhar o inimigo
def draw_enemy():
    pygame.draw.rect(screen, RED, pygame.Rect(target[0]-20, target[1]-20, 40, 40))

# Função principal
def main():
    global target  # Tornar o target uma variável global para atualizar com o mouse
    running = True
    while running:
        screen.fill(BLACK)
        
        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Atualizar a posição do inimigo com a posição do mouse
                target = pygame.mouse.get_pos()

        # Desenhar trajetória e inimigo
        draw_trajectory()
        draw_enemy()
        
        # Atualizar a tela
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
