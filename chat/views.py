from django.shortcuts import render
from django.contrib.auth.models import User
from channels.db import database_sync_to_async

def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})




async def connect(self):
    self.username = await self.get_name()


@database_sync_to_async
def get_name(self):
    return User.objects.all()[0].username
