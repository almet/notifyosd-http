import subprocess
import json

from cornice import Service


notify = Service(name='notify', path='/', description="Notify")


@notify.post()
def send_notify(request):
    data = json.loads(request.body)
    # The options are passed as JSON.
    cmd = ['/usr/bin/notify-send']
    for option in ('expire-time', 'icon', 'urgency', 'category'):
        value = data.get(option)
        if value is not None:
            cmd.append('--%s=%s' % (option, value))

    summary = data.get('summary')
    message = data.get('message')
    if summary:
        cmd.append('%s' % summary)
    if message:
        cmd.append('%s' % message)

    print cmd

    subprocess.Popen(cmd)
    return "ok"
