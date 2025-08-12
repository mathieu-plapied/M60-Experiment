### Commande docker pour environnement local (dev)

Build le docker

```bash
docker build -f dockerfile.dev \
             --platform=linux/arm64 \
             -t mathieup1/m60-exp:dev-cpu .
````

Run le docker
```bash
docker run --rm -it \
  -p 8888:8888 \
  -v "$(pwd)":/workspace \
  -v "$(pwd)/data":/workspace/data \
  mathieup1/m60-exp:dev-cpu
```

### Commande docker distant Runpod (prod)

```bash

```