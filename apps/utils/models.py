from django.db.models import Model, DateTimeField


class TimestampedModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if update_fields:
            if isinstance(update_fields, (set, tuple)):
                update_fields = list(update_fields)
            update_fields.append('updated_at')
        super().save(force_insert, force_update, using, update_fields)
