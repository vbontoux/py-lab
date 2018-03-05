import logging

FORMAT = "[%(asctime)s %(levelname)s %(filename)s:%(lineno)s] %(message)s"
logging.basicConfig(filename='example.log', level=logging.DEBUG, format=FORMAT)
logroot = logging.getLogger('root')
log = logging.getLogger(__name__)


logging.debug('Hello debug')
logging.info('Hello info')
logging.warning('Hello warning')
logging.error('Hello error')

logroot.debug('logger root Hello debug')
logroot.info('logger root Hello info')
logroot.warning('logger root Hello warning')
logroot.error('logger root Hello error')

log.debug('log Hello debug')
log.info('log Hello info')
log.warning('log Hello warning')
log.error('log Hello error')

log.setLevel(logging.ERROR)
log.error('log setLevel to ERROR into default handler')
log.warning('This should never be displayed.')

log.addHandler(logging.StreamHandler())
log.error('log addHandler to go to the console')
log.warning('This should never be displayed.')

