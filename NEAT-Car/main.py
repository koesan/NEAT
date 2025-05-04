import pygame
import os
import math
import sys
import neat

# Resmin boyutları
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
# Resim boyunda pencere oluştur
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Resim pencereye ekle
TRACK = pygame.image.load(os.path.join("img", "map.png"))

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Araba resmi
        self.original_image = pygame.image.load(os.path.join("img", "arac.png"))
        # Ölçekleme faktörü ile arabanın boyu küçültülüyor
        scale_factor = 1.0
        self.original_image = pygame.transform.scale(self.original_image, (int(self.original_image.get_width() * scale_factor), int(self.original_image.get_height() * scale_factor)))
        self.image = self.original_image
        # Arabanın merkez kordinatları atanıyor. Başlangıç konumu.
        self.rect = self.image.get_rect(center=(200, 600))
        # Arabanın hızı ayarlanıyor
        self.vel_vector = pygame.math.Vector2(0.8, 0)
        # Araba resmini açısı
        self.angle = 0
        # Araba hareket ediyormu
        self.drive_state = False
        self.rotation_vel = 5
        # Arabanın direksiyon değeri (sağ 1 sol -1)
        self.direction = 0
        # Aracın alanın dışına çıkmadığını gösteren değişken
        self.alive = True
        # Radar verileri modele sokmak için bir liste tanımla
        self.radars = []
    
    # Aracın istenilen alanın dışına çıkıp çıkmadığını kontrol eder
    def collision(self):
        # Aracın merkezi ile çarpışma noktası arası mesafe
        length = 30
        #aracın sağ ve sol çarpışma noktası'nın kordinatı.
        collision_point_right = [int(self.rect.center[0] + math.cos(math.radians(self.angle + 18)) * length), int(self.rect.center[1] - math.sin(math.radians(self.angle + 18)) * length)]
        collision_point_left = [int(self.rect.center[0] + math.cos(math.radians(self.angle - 18)) * length), int(self.rect.center[1] - math.sin(math.radians(self.angle - 18)) * length)]
        # Arabanın farlarının altında kalan renk, (128,197,106) renk değerine eşit olup olmadığınabakar. Eşit değilse alive değişkenini False yapar
        if SCREEN.get_at(collision_point_right) == pygame.Color(128,197,106, 255) or SCREEN.get_at(collision_point_left) == pygame.Color(128,197,106, 255):
            self.alive = False

    def update(self):
        # Her seferinde radar listesindeki verileri temizle
        self.radars.clear()
        self.drive()
        self.rotate()
        for radar_angle in (-60, -30, 0, 30, 60):
            self.radar(radar_angle)
        # Aracın istenilen alanda olup olmadığını denetler
        self.collision()
        self.data()

    # Aracı ilerleten kod
    def drive(self):
        # Aracın ileri gitmesini sağlar
        self.rect.center += self.vel_vector * 6

    # Aracın sağa sola dönme işlemini gerçekleştirir. 
    def rotate(self):
        # Direction değeri 1 ise sağa -1 ise sola dön
        if self.direction == 1:
            self.angle -= self.rotation_vel
            self.vel_vector.rotate_ip(self.rotation_vel)

        if self.direction == -1:
            self.angle += self.rotation_vel
            self.vel_vector.rotate_ip(-self.rotation_vel)
        # penceredeki aracı döndürüyor
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)
        self.rect = self.image.get_rect(center= self.rect.center)

    # Aracın yolda olup olmadığını radar noktaları ile bulur. böylece sinir ağlarının inputları elde edilir
    def radar(self,radar_angle):
        # Radarın merkez noktadan uzaklığını temsileder.
        length = 0
        # Aracın merkez kordinatları x ve y değişkenlerine atanıyor
        x = int(self.rect.center[0])
        y = int(self.rect.center[1])
        # x ve y kordinatlarındaki pikselin rengi 128,197,106 mu değilmi diye kontrol eder değilse while döngüsüne giriyor 
        while not SCREEN.get_at((x, y)) == pygame.Color(128,197,106, 255) and length < 100:
            # Length değerini while döngüsünün içinde olduğu sürece 1 artırı
            length += 1
            # length değerine göre x, y değerleni günceller
            x = int(self.rect.center[0] + math.cos(math.radians(self.angle + radar_angle)) * length)
            y = int(self.rect.center[1] - math.sin(math.radians(self.angle + radar_angle)) * length)

        # Noktalar arası mesafeyi tutan değişkend
        dist = int(math.sqrt(math.pow(self.rect.center[0] - x, 2) + math.pow(self.rect.center[1] - y, 2)))
        self.radars.append([radar_angle, dist])

    # Radar listesindeki değerleri int türüne dönüştürür ve inputa aktarır
    def data(self):
        input = [0, 0, 0, 0, 0]
        for i, radar in enumerate(self.radars):
            input[i] = int(radar[1])
        return input

# Verilen index'deki Verileri temizlemek için
def remove(index):
    cars.pop(index)
    ge.pop(index)
    nets.pop(index)

def main(genomes, config):
    global cars, ge, nets
    cars,ge, nets = [], [], []
    # Bu döngüde genomes verilerine göre araba oluşturuyor oluşturulan arabaları cars listesine ekliyor genomları ge ve sinir ağınıda nets listesine ekliyor
    for genome_id, genome in genomes:
        cars.append(pygame.sprite.GroupSingle(Car())) # pygame.sprite.GroupSingle(Car()) ifadesi Car sınıfının örneğini içeren bir sprite grubu(pygamede nesneleri gruplamak ve yönetmek için kullanılır) oluşturur.
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0
    while True:
        # Çarpıya basılınca herşeyi kapatmak için
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Haritayı pencerenin arka plan resmi olarak ayarla
        SCREEN.blit(TRACK, (0, 0))

        # cars listesinde hiç araç yoksa tüm işlemleri bitirir
        if len(cars) == 0:
            break
        #cars listesindeki araçlara bakar ve tüm arabaların fitness(arabaların gösterdiği başarı değeridir) değerini 1 artırır. alive değeri False olanları cars,ge,nets değerlerini siler böylece bir dahaki sefere fitness değeri artmaz ve başarısız oldukları anlaşılır böylece sinir ağı öğrenmiş olur
        for i, car in enumerate(cars):
            ge[i].fitness += 1
            if not car.sprite.alive:
                remove(i)
        # cars listesindeki input verilerini nets e yikler ve çıktı elde eder
        for i, car in enumerate(cars):
            output = nets[i].activate(car.sprite.data()) #  nets[i].activate .activate ile nets e inputlar yüklenir ve car.sprite.data() ile de car değişkenindeki radar verileri modele yüklenir
            # Modelin sonuçlarına göre aracı sağa sola döndürür 
            
            if output[0] > 0.5:
                car.sprite.direction = 1
            if output[1] > 0.5:
                car.sprite.direction = -1
            if output[0] <= 0.5 and output[1] <= 0.5:
                car.sprite.direction = 0
        # Tüm arabalar için verileri günceller
        for car in cars:
            car.draw(SCREEN)
            car.update()
        pygame.display.update()

if __name__ == '__main__':
    # Config.txt dosyasının adresi
    config_path = "config.txt"
    # Config dosyasındaki veriler config değişkenine atanıyor
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    # Popilasyonu oluşturur
    pop = neat.Population(config)
    # Raporlama araçlarının eklenmesi
    pop.add_reporter(neat.StdOutReporter(True)) # neat.StdOutReporter sınıfı, konsola çeşitli istatistikleri yazdırmak için kullanılır true bu çıktıları daha ayrıntılı yapar.
    # İstatislik raporlaması için araç ekle
    stats = neat.StatisticsReporter() # neat.StatisticsReporter sınıfı, evrim süreci boyunca istatistikleri toplamak ve raporlamak için kullanılır.
    pop.add_reporter(stats) # stats değişkeni, istatistikleri tutan bir nesnedir.
    # main fonkisyonu çalıştırılır. 50 kaç jenerasyon çalışacağını gösteriyor. tüm araçlar ölünce ve eyeni araçlar oluşunca 1 jenerasyon sayılıyor
    pop.run(main, 50)
