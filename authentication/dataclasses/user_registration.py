from dataclasses import dataclass

@dataclass
class UserRegistration:
    email: str
    nama: str
    password: str
    role: str
    berat_badan: float = None
    tinggi_badan: float = None
    