# Search image by vector embedding app
This repo set up hosting flask api by Compute Engine service - google cloud. \
This is the api for search function in [InsCook App](https://github.com/Chirox03/InsCook). \
Database is hosted on firebase, each query image will be embedded into vector by [CLIP model](https://github.com/openai/CLIP/tree/main) and used for search with vector embedding (See this [document](https://firebase.google.com/docs/firestore/vector-search) to know more).

## Set up virtual environment
```bash
sudo apt-get update
sudo apt install git pip
python3 -m pip install virtualenv
```
Above line is for Linux Debian.

## Create and activate venv
```bash
python3 -m venv myenv
source myenv/bin/activate
```

## Install flask and gunicorn
```bash
pip3 install --upgrade -r requirements.txt
```

## Start sever by gunicorn
```bash
gunicorn -c gunicorn_config.py  main:app
```
