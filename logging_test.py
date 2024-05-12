import logging
import logging.config


# start the logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log',level=logging.DEBUG)

try:
    import slack_logger as sl
    sh = sl.SlackLoggingHandler()
    sh.setLevel(logging.DEBUG)
    sf = sl.SlackFilter()
    sh.addFilter(sf)
    sf = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    sh.setFormatter(sf)
    logger.addHandler(sh)
except:
    pass


logger.debug('debug message')
