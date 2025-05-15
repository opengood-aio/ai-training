# AI Training

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/opengood-aio/ai-training/master/LICENSE)

Source for AI training for AI engineering and data science enablement

# Setup

## Python Virtual Environment

Create Python virtual environment:

```bash
cd ~/workspace/opengood-aio/ai-training/.venv
python3 -m venv ~/workspace/opengood-aio/ai-training/.venv
source .venv/bin/activate
```

## Install Packages

```bash
python3 -m pip install matplotlib
python3 -m pip install numpy
python3 -m pip install pandas
python3 -m pip install scikit-learn
```

## Create Requirements File

```bash
pip freeze > requirements.txt
```
