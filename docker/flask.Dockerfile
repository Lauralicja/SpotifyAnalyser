FROM python:3.9.16-bullseye

WORKDIR /

RUN pip install spotipy && \ 
    pip install flask[async] && \ 
    pip install aioflask && \
    pip install matplotlib && \
    pip install seaborn


COPY /source/ /code/

CMD ["python", "/code/main.py"]

