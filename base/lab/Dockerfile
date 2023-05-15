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
    libgmp-dev \
    gnupg \
    netbase && \
    curl -sSL https://get.haskellstack.org/ | sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Conda packages
RUN conda install --yes -c conda-forge  \
    nodejs=18 \
    r-base \
    r-irkernel \
    r-plyr \
    r-devtools \
    r-tidyverse \
    r-shiny \
    r-rmarkdown \
    r-forecast \
    r-rsqlite \
    r-reshape2 \
    r-nycflights13 \
    r-caret \
    r-rcurl \
    r-crayon \
    r-randomforest \
    r-htmltools \
    r-sparklyr \
    r-htmlwidgets \
    r-hexbin \
    jupyterhub \
    && \
    conda clean -tip && \
    fix-permissions $CONDA_DIR

# Install IJavascript kernel
RUN npm install -g ijavascript && \
    ijsinstall

ENV CPATH=$CONDA_DIR/include

RUN pip install \
    pari_jupyter \
    scilab-kernel && \
    fix-permissions $CONDA_DIR

# Install Rust Kernel
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    . $HOME/.cargo/env && \
    cargo install evcxr_jupyter && \
    evcxr_jupyter --install

# Install Haskell Kernel

ENV PATH=/home/jovyan/.local/bin:${PATH}

RUN stack setup && \
    stack install gtk2hs-buildtools && \
    stack install --fast ihaskell && \
    ihaskell install --stack

USER root

RUN sed -i 's/"\/usr\/bin\/sage"/"env", "PATH=\/usr\/local\/sbin:\/usr\/local\/bin:\/usr\/sbin:\/usr\/bin:\/sbin:\/bin", "\/usr\/bin\/sage"/' /usr/share/jupyter/kernels/sagemath/kernel.json

ENV CPATH=$CONDA_DIR/include