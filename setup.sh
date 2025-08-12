#!/bin/bash

set -e

# Installer les dépendances Python
pip install --no-cache-dir -r requirements.txt

# Créer le répertoire temporaire
mkdir -p /temp/data

# Copier tous les fichiers .tar
cp /workspace/data/*.tar /temp/data/

# Extraire tous les fichiers .tar
for f in /temp/data/*.tar; do
  tar -xvf "$f" -C /temp/data/
done

echo "Données copiées et extraites. RunPod prêt !"
