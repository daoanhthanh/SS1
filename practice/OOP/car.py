class car:
    '''
        Khi tạo và initialize 1 object class, class attribute không được gán??
    '''
    # class property
    vehicle_name = "xe hoi"
    mau_sac = ""
    kha_nang = 0
    gia_co = ""

    def __init__(self, mau_cua_xe, so_ghe_ngoi, vat_lieu):
        self.mau_sac = mau_cua_xe
        self.kha_nang = so_ghe_ngoi
        self.gia_co = vat_lieu

class plane:
    vehicle_name = "may bay"
    def __init__(self, sai_canh, trong_tai, chieu_dai):
        self.sai_canh = sai_canh
        self.trong_tai = trong_tai
        self.chieu_dai = chieu_dai

toyota = car("red", 19, "Allumium")
airbus = plane("190m", 200, 25)
print("Toyota la {}: color: {}, seats: {}, material: {}".format(toyota.__class__.vehicle_name, toyota.mau_sac, toyota.kha_nang, toyota.gia_co) )
print("Airbus la {}, sai canh {}, trong tai {}tan, chieu dai {}m.".format(airbus.__class__.vehicle_name, airbus.sai_canh, airbus.trong_tai, airbus.chieu_dai))