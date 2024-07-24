FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         python3 \
         ca-certificates \
         python3-pip \
         wget \
         sox \
         libsox-dev

RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.1-1_all.deb
RUN dpkg -i cuda-keyring_1.1-1_all.deb && rm cuda-keyring_1.1-1_all.deb
RUN apt-get update && apt-get -y install cuda-compat-12.5 && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV LD_LIBRARY_PATH="/usr/local/cuda-12.5/compat:${LD_LIBRARY_PATH}"
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

WORKDIR /opt/program
COPY requirements.txt /opt/program
RUN pip3 install -r requirements.txt && \
        pip3 install torchaudio -f https://download.pytorch.org/whl/torch_stable.html && \
        pip3 install sox && \
        rm -rf /root/.cache

COPY serve /opt/program