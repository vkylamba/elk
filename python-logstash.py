import logging
import logstash
import sys

host = '192.168.22.69'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5001, version=1))
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 5001, version=1))

msg = "[2017-06-07T10:34:40.158009+00:00] [unchained-ui-dev] [INFO] [/application/src/server/unchained_ui/cms/api/views.py:42] Socket---Fetching json for page 3"

test_logger.error(msg + "\n")
