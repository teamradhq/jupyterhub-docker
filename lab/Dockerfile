FROM jupyter/datascience-notebook:latest

USER root

RUN pip install \
    scilab-kernel && \
    fix-permissions $CONDA_DIR

USER $NB_UID

COPY ./conda-activate.sh /usr/local/bin/before-notebook.d/

