FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /github_pop_svc
COPY requirements.txt /github_pop_svc/
RUN pip install -r requirements.txt
COPY . /github_pop_svc/