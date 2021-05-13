# ベースイメージ
FROM python:3.7.10-slim-buster

# 以降の RUN, CMD コマンドで使われる作業ディレクトリを指定
WORKDIR /
COPY . /

RUN apt-get update \
  && apt-get install -y mecab \
  && apt-get install -y mecab-ipadic \
  && apt-get install -y libmecab-dev \
  && apt-get install -y mecab-ipadic-utf8 \
  && apt-get install -y swig \
  && apt-get -y install locales \
  && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
RUN pip3 install -U --trusted-host pypi.python.org -r requirements.txt
RUN cp /etc/mecabrc /usr/local/etc/
# RUN pip install -r ./src/requirements.txt

# RUN chmod 744 /startup.sh
# CMD ["/startup.sh"]