# Random Civilization
Selects 'n' random Civ 6 leaders. Get the latest leaders by passing the 'update' argument at runtime.

## Quickstart
$ cd ~/github

$ git clone https://github.com/adamturn/random-civ.git && random-civ

### Docker
$ docker build --tag rciv:1.0 .

$ docker run --rm -i rciv:1.0

### Local Env
(env)$ pip install -r requirements.txt

(env)$ python src/main.py update
