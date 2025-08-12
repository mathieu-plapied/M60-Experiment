# M60HD-Experiment

## Prérequis

- Machine avec GPU Nvidia compatible CUDA
- Docker installé

## Configuration de l'environnement

### 1. Lancer le conteneur Docker

```bash
docker run -it --gpus all -v $(pwd):/workspace runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04
```
Sinon directement via runpod (payant): https://console.runpod.io

### 2. Télécharger les données

Récupérer les fichiers depuis le dataset Stanford Dogs :
- **URL** : http://vision.stanford.edu/aditya86/ImageNetDogs/
- **Fichiers requis** :
  - `Images` (757 MB) - contient toutes les images
  - `lists` - contient la répartition train/test

### 3. Installation

```bash
# Cloner le repository
cd /workspace/
git clone https://github.com/mathieu-plapied/M60-Experiment.git
cd M60-Experiment

# Organiser les données
mkdir -p data/
# Déplacer les dossiers Images/ et lists/ dans data/

# Exécuter le script de configuration
chmod +x setup.sh
./setup.sh
```

## Utilisation

Ouvrir le notebook Jupyter pour lancer l'expérience :

```bash
jupyter notebook stanforddogs_exp.ipynb
```