<div align="center">

# NEAT AI Collection

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![NEAT](https://img.shields.io/badge/NEAT-0.92-green.svg)](https://neat-python.readthedocs.io/)
[![Pygame](https://img.shields.io/badge/Pygame-2.5.2-red.svg)](https://pygame.org)

🧠 **A comprehensive collection of AI projects showcasing evolutionary neural networks**

---

[🇬🇧 English](#English) | [🇹🇷 Türkçe](#türkçe)

</div>

---

## English

## 🇬🇧

### About This Collection

This repository showcases the power of evolutionary artificial intelligence through three distinct projects built using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm. Each project demonstrates how AI can learn complex behaviors from scratch, evolving from random actions to sophisticated strategies through natural selection principles.

NEAT is a powerful evolutionary algorithm that simultaneously evolves both the topology and weights of neural networks. Unlike traditional neural networks with fixed architectures, NEAT starts with minimal networks and gradually adds complexity as needed, making it perfect for reinforcement learning scenarios where the optimal network structure is unknown.

### 🎮 Featured Projects

**🚗 NEAT-Car: Autonomous Driving Evolution**
Watch as artificial intelligence learns to navigate complex racing tracks without any prior knowledge. The AI starts by moving randomly, crashing into walls and making poor decisions. Through evolutionary pressure, successful drivers survive and reproduce, gradually developing sophisticated driving strategies including optimal racing lines, speed control, and collision avoidance.

**🐍 NEAT-Snake: Intelligent Food Hunting**
Experience the classic Snake game reimagined through evolutionary AI. The neural network begins with chaotic movements, often colliding with walls or its own tail. Over generations, the AI evolves to understand spatial relationships, develop efficient pathfinding algorithms, and maximize food collection while avoiding obstacles.

**🏓 NEAT-Pong: Adaptive Game Strategy**
Observe how AI masters the timeless game of Pong through evolutionary learning. Starting with random paddle movements, the neural network gradually develops timing, prediction, and strategic positioning. The AI learns to anticipate ball trajectories and develops increasingly sophisticated playing styles.

### ⚡ Quick Start

#### Installation Requirements
```bash
pip install neat-python==0.92 pygame==2.5.2
```

#### Running the Projects

**Launch NEAT-Car Simulation:**
```bash
cd NEAT-Car
python main.py
```

**Start NEAT-Snake Evolution:**
```bash
cd NEAT-Snake
python main.py
```

**Begin NEAT-Pong Training:**
```bash
cd NEAT-Pong
python main.py
```

### 🔬 How NEAT Works

The NEAT algorithm creates remarkable learning experiences by:

**🧬 Evolutionary Selection**: Only the best-performing networks survive to the next generation, ensuring continuous improvement in AI capabilities.

**🌐 Dynamic Network Growth**: Networks start simple and gradually become more complex, adding nodes and connections only when they provide evolutionary advantages.

**🎯 Fitness-Based Learning**: Each AI agent is evaluated based on performance metrics specific to its task, creating natural selection pressure toward optimal behaviors.

**🔄 Genetic Recombination**: Successful networks share their genetic material, combining proven strategies to create even more capable offspring.

---

## Türkçe

## 🇹🇷 

### Koleksiyon Hakkında

Bu depo, NEAT (NeuroEvolution of Augmenting Topologies) algoritması kullanılarak oluşturulmuş üç farklı proje aracılığıyla evrimsel yapay zekanın gücünü sergiler. Her proje, yapay zekanın sıfırdan nasıl karmaşık davranışlar öğrenebileceğini, rastgele eylemlerden doğal seçilim ilkeleri yoluyla gelişmiş stratejilere nasıl evrildiğini gösterir.

NEAT, sinir ağlarının hem topolojisini hem de ağırlıklarını aynı anda geliştiren güçlü bir evrimsel algoritmadır. Sabit mimarili geleneksel sinir ağlarının aksine, NEAT minimal ağlarla başlar ve gerektiğinde kademeli olarak karmaşıklık ekler, bu da optimal ağ yapısının bilinmediği pekiştirmeli öğrenme senaryoları için mükemmel hale getirir.

### 🎮 Öne Çıkan Projeler

**🚗 NEAT-Car: Otonom Sürüş Evrimi**
Yapay zekanın herhangi bir ön bilgi olmadan karmaşık yarış pistlerinde nasıl gezinmeyi öğrendiğini izleyin. AI rastgele hareket ederek başlar, duvarlara çarpar ve kötü kararlar verir. Evrimsel baskı sayesinde, başarılı sürücüler hayatta kalır ve ürer, kademeli olarak optimal yarış çizgileri, hız kontrolü ve çarpışma kaçınma dahil gelişmiş sürüş stratejileri geliştirir.

**🐍 NEAT-Snake: Akıllı Yiyecek Avcılığı**
Evrimsel AI ile yeniden tasarlanan klasik Yılan oyununu deneyimleyin. Sinir ağı kaotik hareketlerle başlar, genellikle duvarlara veya kendi kuyruğuna çarpar. Nesiller boyunca, AI uzamsal ilişkileri anlayacak, verimli yol bulma algoritmaları geliştirecek ve engelleri önlerken yiyecek toplamayı maksimize edecek şekilde evrimleşir.

**🏓 NEAT-Pong: Uyarlanabilir Oyun Stratejisi**
AI'nın evrimsel öğrenme yoluyla zamansız Pong oyununda nasıl ustalaştığını gözlemleyin. Rastgele raket hareketleriyle başlayan sinir ağı, kademeli olarak zamanlama, tahmin ve stratejik konumlandırma geliştirir. AI, top yörüngelerini öngörmeyi öğrenir ve giderek daha gelişmiş oyun stilleri geliştirir.

### ⚡ Hızlı Başlangıç

#### Kurulum Gereksinimleri
```bash
pip install neat-python==0.92 pygame==2.5.2
```

#### Projeleri Çalıştırma

**NEAT-Car Simülasyonunu Başlat:**
```bash
cd NEAT-Car
python main.py
```

**NEAT-Snake Evrimini Başlat:**
```bash
cd NEAT-Snake
python main.py
```

**NEAT-Pong Eğitimini Başlat:**
```bash
cd NEAT-Pong
python main.py
```

### 🔬 NEAT Nasıl Çalışır

NEAT algoritması şu yöntemlerle dikkat çekici öğrenme deneyimleri yaratır:

**🧬 Evrimsel Seçilim**: Sadece en iyi performans gösteren ağlar bir sonraki nesle hayatta kalır, AI yeteneklerinde sürekli gelişim sağlar.

**🌐 Dinamik Ağ Büyümesi**: Ağlar basit başlar ve kademeli olarak daha karmaşık hale gelir, sadece evrimsel avantaj sağladıklarında düğüm ve bağlantı ekler.

**🎯 Fitness Tabanlı Öğrenme**: Her AI ajanı, görevine özgü performans metriklerine göre değerlendirilir, optimal davranışlara doğru doğal seçilim baskısı yaratır.

**🔄 Genetik Rekombinasyon**: Başarılı ağlar genetik materyallerini paylaşır, kanıtlanmış stratejileri birleştirerek daha yetenekli soylar yaratır.
