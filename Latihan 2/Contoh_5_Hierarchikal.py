class AkunBank:
    def __init__(self, nomor_akun, saldo):
        self.nomor_akun = nomor_akun
        self.saldo = saldo
    
    def get_nomor_akun(self):
        return self.nomor_akun
    
    def get_saldo(self):
        return self.saldo

class AkunTabungan(AkunBank):
    def __init__(self, nomor_akun, saldo, persentase_bunga):
        super().__init__(nomor_akun, saldo)
        self.persentase_bunga = persentase_bunga
    
    def get_persentase_bunga(self):
        return self.persentase_bunga

class CekAkun(AkunBank):
    def __init__(self, nomor_akun, saldo, overdraft_limit):
        super().__init__(nomor_akun, saldo)
        self.overdraft_limit = overdraft_limit
    
    def get_overdraft_limit(self):
        return self.overdraft_limit

# Hierarchical Inheritance
class JointAccount(AkunTabungan):
    def __init__(self, nomor_akun, saldo, persentase_bunga, owners):
        super().__init__(nomor_akun, saldo, persentase_bunga)
        self.owners = owners
    
    def get_owners(self):
        return self.owners
    
at = AkunTabungan("45654575", "RP.10.000.000", "10%")
print("Nomor Akun:",at.get_nomor_akun())
print("Saldo:", at.get_saldo())
print("Persentase Bunga:", at.get_persentase_bunga())
print("=============================")
ca = CekAkun("45654575", "RP.10.000.000", "RP.500.000.000")
print("Nomor Akun:",ca.get_nomor_akun())
print("Saldo:", ca.get_saldo())
print("Overdraft Limit:", ca.get_overdraft_limit())
print("=============================")
ja = JointAccount("45654575", "RP.10.000.000", "5%", ["FADLY", "JOHN"])
print("Nomor Akun:",ja.get_nomor_akun())
print("Saldo:", ja.get_saldo())
print("Persentase Bunga:", ja.get_persentase_bunga())
print("Owners:", ja.get_owners())