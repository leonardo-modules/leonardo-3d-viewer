
from django.apps import AppConfig

default_app_config = 'leonardo_3d_viewer.Config'


LEONARDO_APPS = ['leonardo_3d_viewer']

LEONARDO_WIDGETS = ['leonardo_3d_viewer.widget.'
                    'modelviewer.models.ModelViewerWidget']


class Config(AppConfig):
    name = 'leonardo_3d_viewer'
    verbose_name = "leonardo-3d-viewer"

    def ready(self):
        from leonardo.module.media.models import media
        media.MEDIA_FILE_EXTENSIONS[
            'leonardo_3d_viewer.model'] = ['.stl']
