class Book:
    def __init__(self, judul, penulis, tahunterbit):
        self.judul = judul
        self.penulis = penulis
        self.tahunterbit = tahunterbit

    def __str__(self):
        return f"{self.judul} by {self.penulis}, {self.tahunterbit}"

    def search(self, judul):
        if self.judul.lower() == judul.lower():
            return self
        else:
            return None