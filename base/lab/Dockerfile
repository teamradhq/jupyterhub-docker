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

USER $NB_UID

# Conda packages
# Sage conflicts with the latest jupyterhub, thus we must relax the pinning
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
#    julia  \
    jupyterhub \
    && \
    conda clean -tip && \
    fix-permissions $CONDA_DIR

# Update Node to LTS and install IJavascript kernel
RUN conda install --quiet --yes -c conda-forge nodejs=18 && \
    npm install -g ijavascript && \
    ijsinstall

ENV CPATH=$CONDA_DIR/include

RUN pip install \
    pari_jupyter \
    scilab-kernel && \
    fix-permissions $CONDA_DIR

USER root

RUN sed -i 's/"\/usr\/bin\/sage"/"env", "PATH=\/usr\/local\/sbin:\/usr\/local\/bin:\/usr\/sbin:\/usr\/bin:\/sbin:\/bin", "\/usr\/bin\/sage"/' /usr/share/jupyter/kernels/sagemath/kernel.json

ENV CPATH=$CONDA_DIR/include