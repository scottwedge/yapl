# TFproject :  A simple Tensorflow template repo from Data Science And Deep Learning Experiments

## Table of Contents

* [Getting Started](#getting-started)

**Note** : For exhuastive DS environment setup checkout [https://orionpax00.github.io/blogs/ds/work_environment.html](https://orionpax00.github.io/blogs/ds/work_environment.html)

## Getting Started

### Prerequisites

* Python 3.7 or above
* Docker & docker-compose

### Installation

#### Docker

```sh
git clone https://github.com/orionpax00/tfproject.git
cd docker-compose -f .docker/docker-compose.yml up -d
docker exec -it tf_container bash
```

#### Virtualenv

```sh
git clone https://github.com/orionpax00/tfproject.git
virtualenv -p python3 env
source ./env/bin/activate
pip install -r .require/requirements.txt
pip install -e .
```
