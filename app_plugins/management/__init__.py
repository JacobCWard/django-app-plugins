from django.dispatch import dispatcher
from django.db.models import signals
from commands.sync_plugins import sync_app_plugins
from app_plugins import models as sender_app

def do_sync(*args, **kwdargs):
    sync_app_plugins()

dispatcher.connect(do_sync, sender=sender_app, signal=signals.post_syncdb)

if __name__ == "__main__":
    sync_app_plugins()