# NEAT-AI-Collection

**🇹🇷 NEAT algoritması ile geliştirilmiş yapay zeka projeleri koleksiyonu**  
**🇬🇧 A collection of AI projects built using the NEAT algorithm**

---

## 📌 Açıklama | Description

Bu repoda, [NEAT (NeuroEvolution of Augmenting Topologies)](https://neat-python.readthedocs.io/en/latest/) algoritması kullanılarak geliştirilmiş üç farklı yapay zeka projesi bulunmaktadır:

- 🚗 **NEAT-Car**: Yapay zeka destekli otonom araç simülasyonu  
- 🐍 **NEAT-Snake**: Yiyeceğe ulaşmayı öğrenen evrimsel yılan AI  
- 🏓 **NEAT-Pong**: Kendi kendine Pong oynamayı öğrenen AI

---

This repository includes three AI projects developed using the [NEAT (NeuroEvolution of Augmenting Topologies)](https://neat-python.readthedocs.io/en/latest/) algorithm:

- 🚗 **NEAT-Car**: Self-driving car simulation powered by AI  
- 🐍 **NEAT-Snake**: Evolutionary Snake AI that learns to find food  
- 🏓 **NEAT-Pong**: AI that teaches itself to play Pong

---

## 🧠 Kullanılan Kütüphaneler | Libraries Used

- [`neat-python==0.92`](https://github.com/CodeReclaimers/neat-python)
- [`pygame==2.5.2`](https://www.pygame.org/)

**Kurulum için | Installation:**

```bash
pip install neat-python==0.92 pygame==2.5.2
```

---

## 📁 Projeler | Projects

### 🚗 NEAT-Car

**TR:** Bu projede, yapay zeka aracı nasıl süreceğini sıfırdan öğrenir. Başta rastgele hareket ederken, her nesilde yol dışına çıkmadan daha uzun mesafe gitmeyi öğrenir.  
**EN:** In this project, the AI learns how to drive from scratch. It starts by moving randomly and gradually learns to drive longer distances without veering off the track.

**Çalıştırmak için | To Run:**

```bash
cd NEAT-Car  
pip install neat-python==0.92 pygame==2.5.2
python main.py
```

---

### 🐍 NEAT-Snake

**TR:** Klasik yılan oyununu oynayan bir yapay zeka. Başlangıçta rastgele hareket eder, ancak zamanla yiyeceğe ulaşmanın en verimli yollarını keşfeder.  
**EN:** An AI that plays the classic Snake game. It starts with random moves, but over time evolves to find the most efficient paths to reach the food.

**Çalıştırmak için | To Run:**

```bash
cd NEAT-Snake  
pip install neat-python==0.92 pygame==2.5.2
python main.py
```

---

### 🏓 NEAT-Pong

**TR:** Yapay zeka, raketi topa göre doğru şekilde hareket ettirmeyi öğrenerek oyunda puan kazanmaya başlar. Her nesilde daha akıllı hamleler yapar.  
**EN:** The AI learns to move the paddle based on the ball’s position and starts scoring points. With each generation, it gets smarter and plays better.

**Çalıştırmak için | To Run:**

```bash
cd NEAT-Pong  
pip install neat-python==0.92 pygame==2.5.2
python main.py
```

---

## 📹 Demo

Her proje klasöründe demo videoları ve ekran görüntüleri yer almaktadır.  
Demo videos and screenshots are available inside each project folder.