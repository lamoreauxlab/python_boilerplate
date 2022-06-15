FROM python:3.10

# Install Base dependencies and utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    vim
RUN echo 'alias ll='"'"'ls $LS_OPTIONS -al'"'"'' >> ~/.bashrc
RUN pip install --upgrade pip

# Packages that we need
COPY requirements.txt /app/

WORKDIR /app
# instruction to be run during image build
RUN pip install -r requirements.txt

COPY setup.py .

RUN  python /app/setup.py install


ENTRYPOINT [ "/bin/bash" ]
# ENTRYPOINT ["/usr/local/bin/python", "/app/main.py"]
# CMD ["-c default"]
