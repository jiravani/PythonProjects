class Volume:

    total_volumes = 0
    file_system = ""

    def __init__(self, name, volume_name):

        self.name = name
        self.volume_name = volume_name
        Volume.total_volumes += 1
        print self.name + " " + "{:>10}".format(volume_name)

    def get_volume_name(self):
        print self.volume_name

    def set_file_system(self, file_system):
        Volume.file_system = file_system

    def get_file_system(self):
        return Volume.file_system

    def get_total_volumes(self):
        return Volume.total_volumes

    get_total_volume = staticmethod(get_total_volumes)
    get_file_system = staticmethod(get_file_system)
    set_file_system =  staticmethod(set_file_system)
