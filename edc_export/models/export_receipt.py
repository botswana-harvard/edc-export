from django.db import models

from edc_base.model.fields import UUIDAutoField
from edc_base.model.models import BaseUuidModel
from edc_sync.model_mixins import SyncModelMixin


class ExportReceiptManager(models.Manager):

    def get_by_natural_key(self, export_uuid):
        return self.get(export_uuid=export_uuid)


class ExportReceipt(SyncModelMixin, BaseUuidModel):

    export_uuid = UUIDAutoField(
        editable=False,
        help_text="system field for export tracking.")

    app_label = models.CharField(
        max_length=64)

    object_name = models.CharField(
        max_length=64)

    tx_pk = models.CharField(
        max_length=36)

    timestamp = models.CharField(
        max_length=50,
        null=True)

    received_datetime = models.DateTimeField(
        null=True,
        help_text='date ACK received')

    objects = ExportReceiptManager()

    def __str__(self):
        return '{} {}'.format(self.object_name, self.export_uuid)

    def natural_key(self):
        return (self.export_uuid, )

    def dashboard(self):
        # TODO: get this dashboard url
        return 'dashboard?'

    class Meta:
        app_label = 'edc_export'
        ordering = ('-timestamp', )
