import pygame
import sys
import random
import neat
import math
from scipy.spatial import distance

# Yön tanımları
UP    = (0, -1)
LEFT  = (-1, 0)
RIGHT = (1, 0)
DOWN  = (0, 1)

# Ekran boyutları ve grid boyutları
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRIDSIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRIDSIZE

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (0, 255, 0) 
        self.alive = True

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        run = True
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*GRIDSIZE)) % SCREEN_WIDTH), (cur[1] + (y*GRIDSIZE)) % SCREEN_HEIGHT)
        
        # Yılanın kendine çarpmasını kontrol et
        if len(self.positions) > 2 and new in self.positions[2:]:
            run = False
            self.reset()  # Yılan sıfırlansın

        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        return run
    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRIDSIZE, GRIDSIZE))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)  
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRIDSIZE, GRIDSIZE))

def drawGrid(surface):
    for y in range(0, SCREEN_HEIGHT, GRIDSIZE):
        for x in range(0, SCREEN_WIDTH, GRIDSIZE):
            rect = pygame.Rect(x, y, GRIDSIZE, GRIDSIZE)
            pygame.draw.rect(surface, (255, 255, 255), rect, 1)

def main(genomes, config):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    
    
    food = Food()
    food.position = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))
    for genome_id, genome in genomes:
        # Her genome için farklı bir paddle ve net oluşturulur.
        snake = Snake()
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        # Genomların başlangıç fitness değeri 0
        genome.fitness = 0
        
        run = True
        print("run")
        while run:
            # Pencereyi kapatmak için
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
         
            if genome.fitness < -100:
                break

            data = [
                    snake.direction[0],
                    snake.direction[1],
                    snake.positions[0][0],
                    snake.positions[0][1],
                    food.position[0],
                    food.position[1],
                    int(distance.euclidean(food.position, snake.positions[0])), 
                    int(distance.euclidean([food.position[0]], [snake.positions[0][0]])),  
                    int(distance.euclidean([food.position[1]], [snake.positions[0][1]])) 
                    ]
            
            output = net.activate(data)
            decision = output.index(max(output))

            if event.type == pygame.KEYDOWN:
                # Klavyede tuşa basıldığında
                if event.key == pygame.K_LEFT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    snake.direction = RIGHT
                elif event.key == pygame.K_UP:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN:
                    snake.direction = DOWN
            else:
                # Yılanı hareket ettir
                if decision == 0:  # Yukarı hareket
                    snake.direction = RIGHT
                elif decision == 1:  # Aşağı hareket
                    snake.direction = LEFT
                elif decision == 2:  # Sol hareket
                    snake.direction = DOWN
                elif decision == 3:  # Sağ hareket
                    snake.direction = UP

            run = snake.update()
            genome.fitness -= int((distance.euclidean(food.position, snake.positions[0]))/100)
            print(genome.fitness)
            if snake.get_head_position() == food.position:
                snake.length += 1
                genome.fitness += 100
                food.randomize_position()
            surface.fill((0, 0, 0))
            drawGrid(surface)
            snake.render(surface)
            food.render(surface)
            screen.blit(surface, (0, 0))
            pygame.display.update()
            clock.tick(10)

def neat_(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter() 
    pop.add_reporter(stats) 
    pop.run(main, 50)

if __name__ == '__main__':
    config_path = "./config.txt"
    neat_(config_path)