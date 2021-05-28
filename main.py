"""
    PSEUDOCODE

    1. Buat global variable CARD dengan tipe data array
    2. Buat global variable SCORE_RESULT_LIST dengan tipe data array
    3. Buat global variable SCORE_LIST dengan tipe data array yang berisi [100, 80, 60, 40, 20]
    4. Didalam array CARD isi informasi masing-masing kartu didalam dictionary (terdiri dari 12 kartu dengan dan saling berpasang2an / hanya ada 6 kartu yang unik)
    5. Buat function shuffle dengan menerima parameter card = Card untuk mengacak isi dari variable CARD
    6. Buat function main yang akan menjadi function utama didalam project ini, terima 2 parameter bertipe int yang bernilai antara 0 - 11 (untuk menunjuk ke indeks card yang dipilih)
    7. Didalam function main: 
        - panggil function shuffle simpan kedalam variable shuffled
        - deklarasikan variable last bernilai false
        - deklarasikan variable result_list = []
        - buat looping menggunakan -> (while !last)
            ~ buat kondisi apabila shuffled dengan indeks diambil dari parameter pertama sama dengan shuffled dengan indeks dari parameter kedua
                -> tambahkan nilai true kedalam result_list
                -> hapus nilai shuffled yang berada pada indeks ke parameter pertama dan kedua
            ~ tutup kondisi
            ~ buat kondisi baru untuk mengecek apakah variable shuffled panjangnya sama dengan 0
                -> ubah nilai last = true
            ~ tutup kondisi
        - tutup looping
        - panggil function play dengan menambahkan argumen variable result_list dan argumen kedua bernilai 0, lalu masukan kedalam variable score
        - tambahkan (push) variable score kedalam global variable SCORE_RESULT_LIST
        - return global variable SCORE_RESULT_LIST
    8. Buat function play yang memanggil badan function itu sendiri (Recursive): --> disini menggunakan stack
        - terima 2 parameter yang pertama bertipe array yang setiap nilai didalamnya bertipe boolean masukan kedalam variable result_list, yang kedua variable score bertipe integer
        - deklarasikan variable count = 0
        - buat looping menggunakan -> while(!result_list[count])
            ~ tambahkan 1 kedalam nilai count
        - tutup looping
        - buat kondisi apakah count lebih dari 3
            ~ deklarasikan variable X yang didalamnya menghitung variable count / 3 dan bulatkan nilai kebawah
            ~ ambil nilai dari global variable SCORE_LIST indeks ke variable X dan tambahkan hasilnya ke variable score
        - tutup kondisi
        - buang nilai dalam variable result_list hingga indeks ke-n dengan n = count
        - buat kondisi yang mengecek apakah panjang array dari variable result_list = 0
            ~ return score
        - tutup kondisi
        - return function play dengan memberikan argumen pertama = result_list dan argumen kedua = score
"""