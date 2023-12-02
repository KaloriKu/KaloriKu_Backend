from dataclasses import dataclass

@dataclass
class UserRegistration:
    email: str
    nama: str
    password: str
    role: str
    tingkat_aktivitas: str
    umur: str = None
    gender: str = None
    berat_badan: float = None
    tinggi_badan: float = None
    
    