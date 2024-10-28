class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        
    # Menghitung keliling persegi panjang    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    # Menghitung luas persegi panjang
    def luas(self):
        return self.panjang * self.lebar
    
    # Menampilkan deskripsi objek
    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

try:
    panjang = int(input("Masukkan panjang: "))
    lebar = int(input("Masukkan lebar: "))
    
    if panjang < 0 or lebar < 0:
        raise ValueError("Panjang dan lebar harus lebih besar atau sama dengan 0/harus bernilai positif")
    
    # Membuat objek persegi panjang dengan nilai panjang dan lebar yang dimasukkan
    persegi_panjang = PersegiPanjang(panjang, lebar)
    print(persegi_panjang)
    print("Keliling:", persegi_panjang.keliling(), "cm")
    print("Luas:", persegi_panjang.luas(), "cm²")

except ValueError as e:
    print(e)  # Output: Panjang dan lebar harus lebih besar atau sama dengan 0
