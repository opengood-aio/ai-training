# AI Training

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/opengood-aio/ai-training/master/LICENSE)

Source for AI training for AI engineering and data science enablement

# Setup

## Python Virtual Environment

Create Python virtual environment:

```bash
cd ~/workspace/opengood-aio/ai-training/
python3 -m venv ~/workspace/opengood-aio/ai-training/
source bin/activate
```

## Install Packages

```bash
python3 -m pip install matplotlib
python3 -m pip install numpy
python3 -m pip install pandas
```

## Create Requirements File

```bash
python3 -m pip freeze > requirements.txt
python3 -m pip install -r requirements.txt
```
