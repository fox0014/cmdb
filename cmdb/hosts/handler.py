from . models import Asset


class Host(object):
    def __init__(self):
        self.name = ''

    def get_name(self):
        return Asset.objects.get(id='100').dc_id