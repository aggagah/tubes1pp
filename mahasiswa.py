import re


def show_data(dict_mhs):
    '''
    Tampilkan semua data mahasiswa.
    '''
    print('----Fungsi "show_data" dijalankan----')
    print(f'{"NIM":<10}|{"Nama":<15}|{"Email":<20}')
    print('-'*45)
    for nim, d in dict_mhs['data'].items():
        print(f'{nim:<10}|{d["Nama"]:<15}|{d["Email"]:<20}')
    input('\n\nTekan Enter untuk kembali ke menu utama...')


def add_one_mhs(dict_mhs):
    '''
    Fungsi meminta input nim mahasiswa, jika nim sudah ada di dict_mhs maka tampilkan pesan nim sudah ada lalu fungsi selesai.s
    Jika belum ada di data, maka minta data mahasiswa sesuai field mahasiswa.
    Setiap inputan kemudian dicek validitasnya sesuai pola regex, jika tidak valid, maka minta inputan kembali

    '''
    print('----Fungsi "add_one_mhs" dijalankan----')
    # jawaban anda di bawah ini


def add_many_mhs(dict_mhs):
    '''
    Minta n mahasiswa yang akan diinputkan
    Minta data mahasiswa satu per satu yang dimulai dari NIM dahulu. Lalu cek apakah nim sudah terdaftar. Jika sudah, maka tampilkan pesan lalu minta inputan untuk mahasiswa berikutnya.
    Jika nim belum terdaftar, minta data sesuai label, lalu untuk setiap inputan dicek validitasnya berdasarkan pola regex. Jika tidak valid, minta kembali sampai valid
    '''
    print('----Fungsi "add_many_mhs" dijalankan----')
    # jawaban anda di bawah ini


def update_mhs(dict_mhs):
    '''
    Minta nim mahasiswa. Jika nim terdaftar, tampilkan data eksisting.
    Minta data baru, namun jika field tidak ingin diupdate user dapat mengosongkan saja dan field tersebut tidak akan diubah.
    Jika nim tidak ada, tampilkan pesan
    '''
    print('----Fungsi "update_mhs" dijalankan----')
    # jawaban anda di bawah ini
    nimMahasiswa = input("Masukkan NIM: ")
    if nimMahasiswa in dict_mhs['data']:
        print("Data ditemukan.")
        print(f"Nama\t\t: {dict_mhs['data'][nimMahasiswa]['Nama']}")
        print(f"Email\t\t: {dict_mhs['data'][nimMahasiswa]['Email']}")
        print(f"Password\t\t: {dict_mhs['data'][nimMahasiswa]['Password']}")

        print("\nMasukkan data baru, jika tidak ingi diupdate, biarkan kosong")
        namaBaru = input("Masukkan Nama\t\t: ")
        if namaBaru != '':
            dict_mhs['data'][nimMahasiswa]['Nama'] = namaBaru
        emailBaru = input("Masukkan Email\t\t: ")
        if emailBaru != '':
            dict_mhs['data'][nimMahasiswa]['Email'] = emailBaru
        passBaru = input("Masukkan Password\t: ")
        if passBaru != '':
            dict_mhs['data'][nimMahasiswa]['Password'] = passBaru
    else:
        print("Data tidak ditemukan.")
    input("\n\nTekan Enter untuk kembali ke menu utama...")


def delete_mhs(dict_mhs, dict_submission, dict_grade):
    '''
    Minta nim mahasiswa. Jika nim terdaftar, tampilkan data eksisting.
    Konfirmasi apakah akan dihapus, jika ya, hapus nim mahasiswa, lalu hapus semua data mahasiswa yang ada di dict_submission dan dict_grade.
    Jika nim tidak ada, tampilkan pesan.
    '''
    print('----Fungsi "delete_mhs" dijalankan----')
    # jawaban anda di bawah ini
    nimMahasiswa = input("Masukkan NIM: ")
    if nimMahasiswa in dict_mhs['data']:
        print("Data ditemukan.")
        print(f"Nama\t\t: {dict_mhs['data'][nimMahasiswa]['Nama']}")
        print(f"Email\t\t: {dict_mhs['data'][nimMahasiswa]['Email']}")
        print(f"Password\t\t: {dict_mhs['data'][nimMahasiswa]['Password']}")
        cek = input("Anda yakin ingin mengahpus (Y/N)? ").upper()
        if cek == "Y":
            del dict_mhs['data'][nimMahasiswa]
            for id_activity in dict_submission:
                del dict_submission[id_activity][nimMahasiswa]
            for id_activity in dict_grade:
                del dict_grade[id_activity][nimMahasiswa]
    else:
        print("Data tidak ditemukan.")
        print("\n\n")


def login_mhs(dict_mhs):
    print('----Fungsi "login_mhs" dijalankan----')
    nim = input('Masukkan NIM anda: ')
    pwd = input('Masukkan Password anda: ')
    if nim in dict_mhs['data']:
        if pwd == dict_mhs['data'][nim]['Password']:
            print('Login berhasil!')
            return nim
        else:
            print('Password salah!')
    else:
        print('NIM tidak terdaftar!')
    return ''


def print_to_file(dict_mhs):
    '''
    Print data mahasiswa ke dalam file teks. 1 mahasiswa per baris, dan kolomnya adalah sesuai field, pisahkan dengan tab.
    '''
    print('----Fungsi "print_to_file" dijalankan----')
    # jawaban anda di bawah ini
    try:
        namaFile = open(input("Masukkan nama file: "), "x")
    except FileExistsError:
        print("Nama file sudah ada. Silahkan masukkan yang baru")
        namaFile = open(input("Masukkan nama file: "), "x")
    namaFile.write("Nim\t\tNama\t\t\tEmail\t\t\t\t\tPassword\n")
    for i in dict_mhs['data']:
        namaFile.write(
            f"{i}\t\t{dict_mhs['data'][i]['Nama']}\t\t\t{dict_mhs['data'][i]['Email']}\t\t\t{dict_mhs['data'][i]['Password']}\n")
    print("Penyimpanan berhasil")
    input("\n\nTekan Enter untuk kembali ke menu utama...")


if __name__ == "__main__":
    LAST_ID_ACTIVITY = 2
    NIM_LOGIN = ''
    ADMIN_LOGIN = False

    # key pada dict_mhs['data'] adalah NIM
    dict_mhs = {'field': [('Nama', "^([a-zA-Z]+([ '-]| ')?[a-zA-Z]+){1,4}$"),
                          ('Email',
                           '^([a-z0-9]+[._]?[a-z0-9]+)+[@]\w+[.]\w{2,3}'),
                          ('Password', '^[a-zA-Z0-9]{8,12}$')],
                'data': {'113': {'Nama': 'Dummy', 'Email': 'dummy@telU.com', 'Password': '12345678'},
                         '114': {'Nama': 'Joni', 'Email': 'joni@telU.com', 'Password': '12345678'},
                         '115': {'Nama': 'jeje', 'Email': 'jeje@telU.com', 'Password': '12345678'}
                         }
                }

    # Value pada key 'Activities' berupa list berisi id_activity
    list_topic = [{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities': [0, 1]},
                  {'Title': 'Dummy Topic 2',
                      'Description': 'Ini deskripsi topic 2', 'Activities': [2]}
                  ]

    # key pada dict_activity adalah id_activity
    dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                     1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
                     2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                     }

    # key pada dict_submission adalah id_activity
    dict_submission = {0: {'113': 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'},
                       2: {'113': 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'}
                       }

    # key pada dict_grade adalah id_activity
    dict_grade = {0: {'113': 100}

                  }

    print_to_file(dict_mhs)
