FROM python:3.9-slim-buster
LABEL MAINTAINER=sc765@duke.edu
RUN pip install --upgrade pip &&\
    pip install transformers==4.22.2 && \
    pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116 &&\
    pip install gradio==3.4.0 && \
    pip cache purge
RUN python -c "from transformers import pipeline; pipeline('text-classification',model='bhadresh-savani/bert-base-uncased-emotion', top_k=1)" && \
    python -c "import transformers; transformers.utils.move_cache()"
WORKDIR /app/
# COPY ./interface.py ./
COPY ./input.txt ./
COPY ./batch_sent.sh ./
# COPY write_output.py ./
COPY ./inference.py ./
RUN chmod +x batch_sent.sh

CMD ["bash", "batch_sent.sh", "input.txt", "output.txt"]