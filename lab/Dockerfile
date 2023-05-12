FROM base-jupyter-lab

USER root

USER $NB_UID

# Conda packages
# Sage conflicts with the latest jupyterhub, thus we must relax the pinning
RUN conda install --yes -c conda-forge  \
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

ENV CPATH=$CONDA_DIR/include

RUN pip install \
    pari_jupyter \
    scilab-kernel && \
    fix-permissions $CONDA_DIR

USER root
RUN sed -i 's/"\/usr\/bin\/sage"/"env", "PATH=\/usr\/local\/sbin:\/usr\/local\/bin:\/usr\/sbin:\/usr\/bin:\/sbin:\/bin", "\/usr\/bin\/sage"/' /usr/share/jupyter/kernels/sagemath/kernel.json
USER $NB_UID

COPY ./conda-activate.sh /usr/local/bin/before-notebook.d/
