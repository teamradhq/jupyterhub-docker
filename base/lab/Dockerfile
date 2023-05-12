FROM jupyter/datascience-notebook:latest

USER root

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    tzdata \
    gfortran \
    gcc \
    scilab \
    pari-gp \
    libpari-dev \
    sagemath \
    sagemath-jupyter \
    libgmp-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Update Node to LTS and install IJavascript kernel
RUN conda install --quiet --yes -c conda-forge nodejs=18 && \
    npm install -g ijavascript && \
    ijsinstall && \
    fix-permissions $CONDA_DIR

ENV CPATH=$CONDA_DIR/include