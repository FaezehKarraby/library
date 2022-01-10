from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
import json

from chat.models import Chat


def QA(request):
    chats = Chat.objects.all()
    context = {
        'chats': chats,
    }
    return render(request, 'account/QA.html', context)


@login_required
def change_seen_status(request):
    msg_id = request.GET.get('msg_id')
    if msg_id:
        try:
            msg_id = int(msg_id)
            msg = Chat.objects.get(id=msg_id)
            if msg:
                msg_owner_groups = [gp.name for gp in msg.user.groups.all()]
                requested_user_groups = [gp.name for gp in request.user.groups.all()]
                if 'oprators' in msg_owner_groups and 'customers' in requested_user_groups or \
                        'customers' in msg_owner_groups and 'operators' in requested_user_groups:
                    msg.seen = True
                    msg.save()
        except ValueError:
            return HttpResponseBadRequest('Error: your msg_id must be integer... .')
    response_data = {}
    return HttpResponse(json.dumps(response_data), content_type="application/json")
