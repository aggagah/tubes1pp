def show_all_grade(dict_grade, dict_activity):
    '''
    Tampilkan setiap  aktifitas beserta list nilai mahasiswanya
    '''
    print('----Fungsi "show_all_grade" dijalankan----')
    for k, v in dict_grade.items():
        print(f'ID\t: {k}')
        print(f'Title\t:{dict_activity[k]["Title"]}')
        print(f'Nilai semua mahasiswa: ')
        print(f'{"NIM":<10}|Nilai')
        print('-'*15)
        for nim, nilai in v.items():
            print(f'{nim:<10}|{nilai}')
        print()

    input('\n\nTekan Enter untuk kembali ke menu...')


def show_mhs_not_graded(dict_submission, dict_grade):
    '''
    Tampilkan setiap nim mahasiswa yang memiliki setidaknya satu submission yang belum dinilai
    '''
    print('----Fungsi "show_mhs_not_graded" dijalankan----')
    # jawaban anda di bawah ini


def add_grade_by_mhs(dict_submission, dict_activity, dict_grade):
    '''
    Minta nim 1 mahasiswa
    Cek nim tersebut di semua submission, lalu cek apakah sudah ada nilai. Jika belum, tampilkan detil assignment.
    Tampilkan jawaban mahasiswa, lalu minta nilainya.
    '''
    print('----Fungsi "add_grade_by_mhs" dijalankan----')
    # jawaban anda di bawah ini


def show_assignment_not_graded(dict_submission, dict_activity, dict_grade):
    '''
    Tampilkan setiap data activity assignment yang memiliki setidaknya satu submission mahasiswa yang belum dinilai
    '''
    print('----Fungsi "show_assignment_not_graded" dijalankan----')
    # jawaban anda di bawah ini


def add_grade_by_assignment(dict_submission, dict_grade):
    '''
    Minta ID assignment yang ingin dinilai.
    Tampilkan data nim mahasiswa beserta jawaban yang belum dinilai, lalu minta nilainya
    '''
    print('----Fungsi "add_grade_by_assignment" dijalankan----')
    # jawaban anda di bawah ini
    pilihId = int(input("Masukkan ID assignment yang ingin dinilai: "))
    id_activity = pilihId
    print("NIM\t| Jawaban")
    print("-"*50)
    if id_activity not in dict_grade:
        dict_grade[id_activity] = {}
        for nim in dict_submission[id_activity]:
            dict_grade[id_activity][nim] = ''
            print(f"{nim}\t| {dict_submission[id_activity][nim]}")
            nilai = int(input("Masukkan nilai (0-100): "))
            dict_grade[id_activity][nim] = nilai
    elif id_activity in dict_grade:
        for nim in dict_submission[id_activity]:
            if nim not in dict_grade[id_activity]:
                dict_grade[id_activity][nim] = ''
                print(f"{nim}\t| {dict_submission[id_activity][nim]}")
                nilai = int(input("Masukkan nilai (0-100): "))
                dict_grade[id_activity][nim] = nilai


def report_by_assignment(dict_submission, dict_activity, dict_grade):
    '''
    Tampilkan data rekapan untuk tiap assignment, berupa nilai rata-rata dari semua mahasiswa, banyaknya submission di assignment tersebut, dan banyak submission yang sudah dinilai
    '''
    print('----Fungsi "report_by_assignment" dijalankan----')
    # jawaban anda di bawah ini


def report_by_mhs(dict_submission, dict_grade):
    '''
    Tampilkan data rekapan untuk tiap mahasiswa, berupa nilai rata-rata untuk semua assignment, banyaknya submission oleh mahasiswa, dan banyaknya submission mahasiswa tersebut yang sudah dinilai.
    '''
    print('----Fungsi "report_by_mhs" dijalankan----')
    # jawaban anda di bawah ini


def print_grade_to_file(dict_grade, dict_activity):
    '''
    Minta nama file.
    Tulis semua data grade ke file.
    '''
    print('----Fungsi "print_grade_to_file" dijalankan----')
    # jawaban anda di bawah ini
    try:
        file = open(input("Masukkan nama file: "), "x")
    except FileExistsError:
        print("Nama file yang anda masukkan sudah ada. Masukkan nama lain")
        file = open(input("Masukkan nama file: "), "x")
    for id_activity in dict_activity:
        if id_activity in dict_grade:
            if dict_activity[id_activity]['Type'] == 'assignment':
                file.write(f"ID\t: {id_activity}\n")
                file.write(f"Title\t: {dict_activity[id_activity]['Title']}\n")
                file.write("Nilai semua mahasiswa:\n")
                file.write("NIM   | Nilai\n")
                for nim in dict_grade[id_activity]:
                    file.write(f"{nim}   | {dict_grade[id_activity][nim]}\n")
        else:
            pass
        file.write("\n")


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

