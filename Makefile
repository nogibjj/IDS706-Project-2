install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

format:
	black *.py

lint:
	pylint --disable=R,C,W1203,W1202 *.py
test:

all: install format lint test