__author__ = 'flaviocaetano'

from django.conf import settings

import sys
import threading

def get_pelican_settings_file():
    return getattr(settings, 'PELICAN_SETTINGS', 'pelicanconf')

#
# KThread.py: A killable Thread implementation.
#

class KThread(threading.Thread):
    """A subclass of threading.Thread, with a kill()
    method."""
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        self.run = self.__run # Force the Thread to install our trace.
        threading.Thread.start(self)

    def __run(self):
        """Hacked run function, which installs the
        trace."""
#        if not settings.DEBUG:
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True