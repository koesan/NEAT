import pygame
import sys
import random
import pickle
import neat
import time

# Pencere boyutu
WIDTH, HEIGHT = 700, 500

BLACK = (20, 20, 20)
WHITE = (255, 255, 255)

# Raket sınıfı
class Paddle(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    # Raketin hareket fonksiyonu    
    def move(self,keys):
        fitness = 0

        if keys == 0 and self.rect.top > 0:
            self.rect.y -= 8
            time.sleep(0.01)

        elif keys == 1 and self.rect.bottom < HEIGHT:
            self.rect.y += 8
            time.sleep(0.01)

        else :
            fitness = -0.1 # Sabit kalmaması için
        return fitness

# Top sınıfı
class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = [random.choice([4, -4]), random.choice([4, -4])]

    # Çarpışma kontrolü
    def collide(self):
        fitness = 0
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        # Topun ekranın üst veya alt kenarına çarparsa
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.x += self.speed[0] 

        # Topun ekran'nın sol kenarına çarparsa
        elif self.rect.left <= 1: 
            self.rect.center = (WIDTH // 2, HEIGHT // 2)
            self.rect.x += self.speed[0] 
            self.speed[0] = random.choice([4, -4])
            self.speed[1] = random.choice([4, -4])
            fitness = -100

        # Top pencere'nin sağ kenarına çarparsa 
        elif self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0] 

        return fitness

def main(genomes, config):

    # Pygame'ı başlat
    pygame.init()

    # Pygame ekranını oluştur
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong Game")

    # Font ve renk tanımlamaları
    font = pygame.font.Font(None, 36)
    text_color = WHITE

    # Top nesnesini oluştur
    ball = Ball()

    # Oyun döngüsü
    clock = pygame.time.Clock()

    for genome_id, genome in genomes:
        # Her genome için farklı bir paddle ve net oluşturulur.
        paddle = Paddle(20, HEIGHT // 2)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        # Genomların başlangıç fitness değeri 0
        genome.fitness = 0
        
        run = True
        while run:
            # Pencereyi kapatmak için
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # genome.fitness değeri -100 den küçük ise sonraki genoma geç
            if genome.fitness <= -100:
                run = False

            # Modelin inputları alınıyor(paddle'nin y kordinatı, paddle'nin x kordinatı, ball'ın x değeri arasındaki mesafenin mutlak değeri ve ball'ın y kordiantı)
            data = [paddle.rect.center[1], abs(paddle.rect.center[0] - ball.rect.center[0]), ball.rect.center[1]]
            output = net.activate(data) #net'e inputlar yüklenerek eğitiliyor ve çıktı alınıyor
            decision = output.index(max(output)) # Çıktıda en büyük değere sahip veri'nin indeksi alınıyor
            genome.fitness += paddle.move(decision) # Raketi hareket ettirmek için decision değeri move fonksiyonuna gönderiliyor ve döndürülen fitnes değeri genome.fitness'a ekleniyor
            genome.fitness += ball.collide() # Ball nesnesinin çarpışması kontrol ediliyor ve döndürülen değer genome.fitness'a ekleniyor

            # Raket ile topun çarpışması kontrole diliyor
            if pygame.sprite.collide_rect(ball, paddle):
                genome.fitness += 100 # Top rakete çarpmışsa fitnes değeri artar
                ball.speed[0] = -ball.speed[0] # Topun hızını tes çevri
                ball.rect.x += ball.speed[0] # Topun Raketin içine girmemesi için 
            
            # Ekranı siyaha boya
            screen.fill(BLACK)
            # ball ve paddle nesnelerini ekrana çiz
            pygame.draw.rect(screen, WHITE, ball.rect)
            pygame.draw.rect(screen, WHITE, paddle.rect)

            # Fitness Değerini ekrana yazdır
            fitness_text = font.render(f'Fitness: {int(genome.fitness)}', True, text_color)
            screen.blit(fitness_text, (500, 10))  
            # Ekranını güncelle 
            pygame.display.flip()
            clock.tick(60)

def neat_(config_path):

    # Config dosyasındaki veriler config değişkenine atanıyor
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    # Popilasyonu oluşturur
    pop = neat.Population(config)
    # Raporlama araçlarının eklenmesi
    pop.add_reporter(neat.StdOutReporter(True)) # Konsola çeşitli istatistikleri yazdırmak için kullanılır.
    # İstatislik raporlaması için araç ekle
    stats = neat.StatisticsReporter() # Evrim süreci boyunca istatistikleri toplamak ve raporlamak için kullanılır.
    pop.add_reporter(stats)
    # main fonkisyonu çalıştırılır. 50 kaç jenerasyon çalışacağını gösteriyor.
    winner = pop.run(main, 50) # En iyi sonucu döndürür
    # Modeli kaydet
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)

if __name__ == '__main__': 
    # Config.txt dosyasının adresi
    config_path = "config.txt"
    neat_(config_path)
