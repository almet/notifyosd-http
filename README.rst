Notify OSD HTTP
===============

This is a simple webservice so that it's possible to send NotifyOSD messages to
your desktop over HTTP.

The goal is to make this work for email / twitter / facebook etc. notifications
so that you stop going there to see if you have new messages :-)

::

    >>> import requests
    >>> requests.post('http://0.0.0.0:6543',
                      data=json.dumps({'message': 'test', 'icon': 'info'}))

And you should see this:

.. image:: http://alexis.notmyidea.org/notif.png

