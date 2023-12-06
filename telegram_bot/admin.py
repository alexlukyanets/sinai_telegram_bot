from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import TelegramUser, TextLanguages, MenuItem, DataBotText, MenuLevel


@admin.register(TelegramUser)
class TelegramUserAdmin(ModelAdmin):
    list_filter = ('is_admin', 'is_blocked_bot', 'created_at')
    search_fields = ('username', 'first_name', 'last_name')
    readonly_fields = ('tg_user_id', 'username', 'first_name', 'last_name', 'language_code', 'is_blocked_bot',
                       'created_at')

    class Meta:
        fields = '__all__'


@admin.register(MenuLevel)
class MenuLevelsAdmin(ModelAdmin):
    list_filter = ('developed',)
    prepopulated_fields = {'level_text_id': ('level_name',)}

    class Meta:
        fields = '__all__'


@admin.register(MenuItem)
class MenuItemAdmin(ModelAdmin):
    ordering = ('position_in_row', 'position_in_col',)
    prepopulated_fields = {'name_of_execution_function': ('text',)}
    search_fields = ('text', 'name_of_execution_function')
    save_as = True
    save_on_top = True
    list_display = (
        'text', 'name_of_execution_function', 'position_in_row', 'position_in_col', 'level',
        'language', 'created_at',
        'updated_at')
    list_display_links = ('text', 'name_of_execution_function')

    list_filter = ['level']


@admin.register(TextLanguages)
class TextLanguagesAdmin(ModelAdmin):
    class Meta:
        fields = '__all__'


@admin.register(DataBotText)
class TextBotAdmin(ModelAdmin):
    prepopulated_fields = {'id_value': ('text',)}
    search_fields = ('text', 'id_value')
    list_filter = ('created_at',)
    list_display = (
        'text', 'id_value', 'language', 'created_at', 'updated_at')
