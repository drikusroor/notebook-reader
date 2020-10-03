# Powershell

## How to use

### Build container

```ps
docker build -t ainab/notebook-reader .
```

### Run container with volume (execute from root of project)

```ps
docker run -it -v ${PWD}/src:/usr/src/app/src ainab/notebook-reader
```

Then, using bash:

```bash
cd src
python main.py
```

## Based on https://github.com/gtsoukas/scene_text
