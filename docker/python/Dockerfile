# ベースイメージ
FROM python:3.9.5-slim-buster

# 以降の RUN, CMD コマンドで使われる作業ディレクトリを指定
WORKDIR /
COPY . /

RUN apt-get update \
  && apt-get install -y mecab \
  && apt-get install -y mecab-ipadic \
  && apt-get install -y libmecab-dev \
  && apt-get install -y mecab-ipadic-utf8 \
  && apt-get install -y swig

RUN pip install --trusted-host pypi.python.org -r requirements.txt
# RUN pip install -r ./src/requirements.txt

# RUN chmod 744 /startup.sh
# CMD ["/startup.sh"]