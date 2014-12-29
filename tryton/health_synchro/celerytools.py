import os
import subprocess
import tempfile
from trytond.model import ModelSQL
from trytond.transaction import Transaction
from trytond.config import CONFIG

__all__ = ['Sync']

celery_available = None
try:
    import celery as celery_available
except ImportError:
    pass
except AttributeError:
    # If run from within frepple we will get
    # AttributeError: 'module' object has no attribute 'argv'
    pass

def start_celery():
    celery_start = CONFIG.get('celery_start', True)
    if celery_available is None or not celery_start:
        return
    db = Transaction().cursor.database_name
    env = {
        'TRYTON_DATABASE': db,
        'TRYTON_CONFIG': CONFIG.configfile
    }
    print "env", env
    #Copy environment variables in order to get virtualenvs working
    for key, value in os.environ.iteritems():
        env[key] = value
    call = ['celery', 'worker', '--app=celery_synchronisation', 
        '--loglevel=info',
        '--workdir=/tmp', '--queues=' + db,
        '--time-limit=7400',
        '--concurrency=1',
        '--hostname=' + db + '.%h',
        '--pidfile=' + os.path.join(tempfile.gettempdir(), 'trytond_celery_' +
            db + '.pid')]
    subprocess.Popen(call, env=env)


class Sync(ModelSQL):
    "Sync"
    __name__ = 'health.sync'

    @classmethod
    def __setup__(cls):
        super(Sync, cls).__setup__()
#        start_celery()
        

def sync():
    pool = Pool()
    transaction = Transaction()
    cursor = transaction.cursor
    
    #result = os.system('celery call tryton_synchronisation.synchronise_push_all '
    #            '--args=[%d,%d] '
    #            '--config="trytond.modules.health_synchro.celeryconfig" '
    #            '--queue=%s' % (
    #                execution.id, transaction.user, cursor.database_name))
    #        if result != 0:
    #            #Fallback to concurrent mode if celery is not available
    #            Execution.calculate([execution])
