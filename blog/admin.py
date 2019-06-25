from django.contrib import admin
from .models import Character, RespostaPost, Aventura, Post


admin.site.register(Aventura)
admin.site.register(Post)
admin.site.register(Character)
admin.site.register(RespostaPost)

