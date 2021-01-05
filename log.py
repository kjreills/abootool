import sys
import logging
from config import Config

level = logging.INFO
TRACE = 9

l = logging.getLogger("ABOOTOOL")


con = logging.StreamHandler(sys.stderr)
con.setFormatter(logging.Formatter('%(levelname)1s: %(message)s'))
con.setLevel(level)

logfile = logging.FileHandler(Config.)
logfile.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)5s: %(message)s'))
logfile.setLevel(logging.DEBUG)

l.addHandler(con)
l.addHandler(logfile)
l.setLevel(TRACE)


logging.addLevelName(TRACE, "TRACE")


def adjustLevels():
    for log in logging.Logger.manager.loggerDict:
        l.setLevel(logging.CRITICAL)

    for h in logging.root.handlers:
        logging.root.removeHandler(h)

    l.setLevel(TRACE)


def setVerbose(more = False):
    global level
    level = more and TRACE or logging.DEBUG
    logfile.setLevel(level)


def I(msg, *kargs, **kwargs):
    l.info(msg, *kargs, **kwargs)


def D(msg, *kargs, **kwargs):
    l.debug(msg, *kargs, **kwargs)


def T(msg, *kargs, **kwargs):
    l.log(TRACE, msg, *kargs, **kwargs)


def W(msg, *kargs, **kwargs):
    l.warn(msg, *kargs, **kwargs)


def E(msg, *kargs, **kwargs):
    l.error(msg, *kargs, **kwargs)
