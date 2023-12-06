from django.db import models

default_dict = dict(null=True, blank=True)


class TelegramUser(models.Model):
    tg_user_id = models.PositiveBigIntegerField(primary_key=True,
                                                verbose_name="Telegram User ID")  # rename to telegram id
    username = models.CharField(max_length=32, **default_dict, verbose_name="Telegram Username")
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, **default_dict)
    language_code = models.CharField(max_length=8, help_text="Telegram client's lang", **default_dict)
    is_blocked_bot = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects: models.manager.BaseManager["TelegramUser"]

    class Meta:
        db_table = "tg_user"
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'
        ordering = ['created_at']

    def __str__(self):
        if self.username:
            return f"{self.username}"
        return f"{self.tg_user_id}"


class TextLanguages(models.Model):
    name = models.CharField(max_length=256)
    language_code = models.CharField(max_length=8, help_text="language code", primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.language_code}"

    class Meta:
        db_table = "text_languages"
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['created_at']


class MenuLevel(models.Model):
    menu_level_id = models.AutoField(primary_key=True,
                                     verbose_name="Menu Level ID")
    level_name = models.CharField(max_length=256)
    parent = models.ForeignKey('self', related_name='sub_level', on_delete=models.CASCADE, **default_dict)
    keyboard_type = models.CharField(
        max_length=10,
        choices=[('inline', 'Inline Keyboard'), ('reply', 'Reply Keyboard')], default='inline')
    developed = models.BooleanField(default=False)
    level_text_id = models.CharField(max_length=100, **default_dict)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.level_name}"

    class Meta:
        db_table = "menu_level"
        verbose_name = 'Menu Level'
        verbose_name_plural = 'Menu Levels'
        ordering = ['created_at']


class MenuItem(models.Model):
    name_of_execution_function = models.CharField(max_length=100, primary_key=True)
    position_in_row = models.IntegerField(default=0)
    position_in_col = models.IntegerField(default=0)
    level = models.ForeignKey(MenuLevel, on_delete=models.CASCADE)
    text = models.TextField()
    text_reply = models.TextField(**default_dict)
    menu_reply = models.ForeignKey(MenuLevel, on_delete=models.CASCADE, related_name='menu_reply_items', **default_dict)
    language = models.ForeignKey(TextLanguages, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text} - {self.name_of_execution_function}"

    class Meta:
        db_table = "menu_item"
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'
        ordering = ['created_at']


class DataBotText(models.Model):
    data_bot_text_id = models.AutoField(primary_key=True)
    text = models.TextField()
    id_value = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.ForeignKey(TextLanguages, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_value} - {self.text}"

    class Meta:
        db_table = "data_bot_text"
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'
        ordering = ['created_at']
