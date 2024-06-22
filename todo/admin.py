from django.contrib import admin
from todo.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Description', 'user', 'created_at')  # Zeigt created_at in der Listenansicht an
    fields = ('Title', 'Description', 'created_at', 'user')  # Felder, die bearbeitbar sind
    search_fields = ['Title', 'Description']

# Register your models here.
admin.site.register(Todo, TodoAdmin)
