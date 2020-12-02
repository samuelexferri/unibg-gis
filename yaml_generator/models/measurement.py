class Measurement:
    def __init__(self, name, dtype, units, nodata=0, path="dataset.nc", layer=""):
        self.name = name
        self.dtype = dtype
        self.units = units
        self.path = path
        self.nodata = nodata
        self.layer = layer if layer != "" else name
