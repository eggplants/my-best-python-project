FROM python:3

RUN pip install --upgrade pip

RUN python -m pip install git+https://github.com/eggplants/my-best-python-project

ENTRYPOINT ["mbpp"]
