Definisikan fungsi objektif f(x) = x^2

Inisialisasi parameter:
    jumlah_partikel = 10
    iterasi_maks = 50
    batas_bawah = -10
    batas_atas = 10
    w = 0.5             // inersia
    c1 = 1.5            // koefisien kognitif
    c2 = 1.5            // koefisien sosial

Inisialisasi:
    Untuk setiap partikel:
        - Inisialisasi posisi acak di antara batas_bawah dan batas_atas
        - Inisialisasi kecepatan awal = 0
        - Hitung fitness awal (f(x))
        - Simpan posisi terbaik pribadi (pbest) = posisi awal

    Tentukan posisi terbaik global (gbest) dari semua pbest

Untuk iterasi = 1 hingga iterasi_maks:
    Untuk setiap partikel:
        - Hasilkan dua bilangan acak r1 dan r2 dari [0, 1]
        - Perbarui kecepatan:
            v = w * v + c1 * r1 * (pbest - posisi) + c2 * r2 * (gbest - posisi)
        - Perbarui posisi:
            posisi = posisi + v
            Jika posisi < batas_bawah → setel posisi = batas_bawah
            Jika posisi > batas_atas → setel posisi = batas_atas
        - Hitung fitness baru f(posisi)
        - Jika fitness baru < pbest_fitness:
            Perbarui pbest = posisi sekarang
            Jika fitness baru < gbest_fitness:
                Perbarui gbest = posisi sekarang

    Simpan gbest_fitness ke dalam riwayat iterasi

Setelah selesai:
    Cetak gbest dan gbest_fitness
    Plot grafik konvergensi: fitness terbaik vs iterasi
