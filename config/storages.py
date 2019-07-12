from storages.backends.azure_storage import AzureStorage
import os


class StaticStorage(AzureStorage):
    overwrite_files = True
    azure_container = 'static-dev'


class MediaStorage(AzureStorage):
    overwrite_files = True
    azure_container = os.environ.get('AZURE_CONTAINER')
