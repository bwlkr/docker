FROM sebp/elk

#WORKDIR ${LOGSTASH_HOME}
RUN gosu logstash bin/logstash-plugin install logstash-input-gelf && rm -f /etc/logstash/conf.d/*

COPY gelf.conf /etc/logstash/conf.d/gelf.conf