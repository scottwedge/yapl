## Getting Started

### Prerequisites
* Python 3.7 or above
* Docker & docker-compose

### Installation
#### Docker

```sh
git clone https://github.com/orionpax00/tfproject.git
```
```sh
cd docker-compose -f .docker/docker-compose.yml up -d
```
To go inside container
```sh
docker exec -it tf_container bash
```

#### Virtualenv

```sh
git clone https://github.com/orionpax00/tfproject.git
```
```sh
virtualenv -p python3 env
```
```sh
source ./env/bin/activate
```
```sh
pip install -r .require/requirements.txt
```
```sh
pip install -e .
```