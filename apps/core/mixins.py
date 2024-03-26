from django.conf import settings


class AttachmentMixin(object):

    @property
    def attachment_url(self):
        if self.attachment:
            return self.attachment.url

    @property
    def attachment_storage_backend(self):
        return settings.DEFAULT_FILE_STORAGE
