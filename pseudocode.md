# (Opsional) Set seed agar hasil acak konsisten setiap dijalankan
set_random_seed(42)

# Inisialisasi partikel dan parameter
posisi = [random dalam batas pencarian untuk setiap partikel]
kecepatan = [0.0 untuk setiap partikel]
pBest = posisi.copy()
fitness_pBest = [evaluasi(p) untuk p dalam pBest]
gBest = pBest dengan fitness terbaik

# Iterasi utama algoritma PSO
for iterasi in range(jumlah_iterasi):

# Update pBest untuk setiap partikel
    for i in range(jumlah_partikel):
        fitness = evaluasi(posisi[i])
        if fitness < fitness_pBest[i]:
            pBest[i] = posisi[i]
            fitness_pBest[i] = fitness

# Update gBest dari pBest terbaik
    gBest = pBest dengan fitness terbaik

# Update kecepatan dan posisi partikel
    for i in range(jumlah_partikel):
        r1 = random antara 0 dan 1
        r2 = random antara 0 dan 1

        kecepatan[i] = (
            w * kecepatan[i]
            + c1 * r1 * (pBest[i] - posisi[i])
            + c2 * r2 * (gBest - posisi[i])
        )

        posisi[i] += kecepatan[i]

# Clamp posisi agar tetap dalam batas
        if posisi[i] < batas_min:
            posisi[i] = batas_min
        elif posisi[i] > batas_max:
            posisi[i] = batas_max

# Simpan fitness terbaik saat ini (opsional untuk visualisasi)
    simpan evaluasi(gBest)
