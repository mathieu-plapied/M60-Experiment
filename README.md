# M60HD-Experiment
Le PDF complet du mémoire est disponible ici : [M60HD Mémoire PDF](M60HD.pdf)
## Abstract du mémoire

Dans un cadre de transfer learning sur CNN, ce mémoire étudie comment l’optimisation multiobjectif des hyperparamètres avec NSGA-II et Optuna permet de créer un front de Pareto exactitude-énergie et d’identifier un compromis adapté. L’espace de recherche couvre des hyperparamètres clés de l’entrainement comme le learning rate du backbone et du classifier, la weight decay, le dropout, la taille de batch et le nombre de blocs dégelés. L’analyse fANOVA met en évidence que l’énergie d’entraînement dépend surtout du nombre de blocs dégelés, avec près de 93% de la variance, tandis que l’exactitude est principalement déterminée par le learning rate du backbone, autour de 91%. Le front de Pareto observé est concave et présente des rendements décroissants. À mesure que l’exactitude augmente, l’efficacité énergétique diminue. Un point de genou atteint 98% de l’exactitude maximale tout en réduisant d’environ 31% l’énergie par image. La portée est volontairement limitée à un modèle et un jeu de données, et seule l’énergie d’entraînement est mesurée.

## Excuter le code

### Prérequis

- Machine avec GPU Nvidia compatible CUDA
- Docker installé

### Configuration de l'environnement

#### 1. Lancer le conteneur Docker

```bash
docker run -it --gpus all -v $(pwd):/workspace runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04
```
Sinon directement via runpod (payant): https://console.runpod.io

#### 2. Télécharger les données

Récupérer les fichiers depuis le dataset Stanford Dogs :
- **URL** : http://vision.stanford.edu/aditya86/ImageNetDogs/
- **Fichiers requis** :
  - `Images` (757 MB) - contient toutes les images
  - `lists` - contient la répartition train/test

#### 3. Installation

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

### Utilisation

Ouvrir le notebook Jupyter pour lancer l'expérience :

```bash
jupyter notebook stanforddogs_exp.ipynb
```