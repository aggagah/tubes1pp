def show_topic(list_topic, dict_activity):
    '''
    Menampilkan setiap topik beserta detil aktifitasnya
    '''
    print('----Fungsi "show_topic" dijalankan----')
    # jawaban anda di bawah ini
    for i in list_topic:
        print(f"Title\t: {i['Title']}")
        print(f"Description: {i['Description']}")
        print("List activity:")
        print("ID\t| Title\t\t\t| Type\t\t| Description")
        print(
            "----------------------------------------------------------------------")
        for j in i['Activities']:
            if len(dict_activity[j]['Title']) > 14:
                if len(dict_activity[j]['Type']) < 10:
                    print(
                        f"{j}\t| {dict_activity[j]['Title']}\t| {dict_activity[j]['Type']}\t\t| {dict_activity[j]['Description']}")
                elif len(dict_activity[j]['Type']) >= 10:
                    print(
                        f"{j}\t| {dict_activity[j]['Title']}\t| {dict_activity[j]['Type']}\t| {dict_activity[j]['Description']}")
            elif len(dict_activity[j]['Title']) <= 14:
                if len(dict_activity[j]['Type']) < 10:
                    print(
                        f"{j}\t| {dict_activity[j]['Title']}\t| {dict_activity[j]['Type']}\t| {dict_activity[j]['Description']}")
                elif len(dict_activity[j]['Type']) >= 10:
                    print(
                        f"{j}\t| {dict_activity[j]['Title']}\t\t| {dict_activity[j]['Type']}\t| {dict_activity[j]['Description']}")
        print("\n")
    input("\n\nTekan Enter untuk kembali ke menu utama...")


def add_topic(list_topic, dict_activity, id_activity):
    '''
    Meminta data topik baru. Menambahkan topik baru ke list_topic.
    Tanya jika ingin sekaligus menambahkan actifitas. Jika menambahkan aktifitas, naikkan counter id_activity dengan 1,
    baru dijadikan sebagai key activity baru.

    Return id_activity yang terakhir digunakan

    '''
    print('----Fungsi "add_topic" dijalankan----')
    # jawaban anda di bawah ini


def delete_topic(list_topic, dict_activity, dict_submission, dict_grade):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin dihapus.
    Lalu hapus topik beserta semua aktivitasnya, hapus juga data di activity, submission, dan grade untuk id aktivitas yang terdapat di topik ini
    '''
    print('----Fungsi "delete_topic" dijalankan----')
    # jawaban anda di bawah ini


def update_topic(list_topic):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin diupdate.
    Tampilkan data eksisting.
    Minta data update ke user, jika field tidak ingin diupdate, user cukup mengosongkan field
    '''
    print('----Fungsi "update_topic" dijalankan----')
    # jawaban anda di bawah ini
    count = 1
    listNomor = []
    for i in list_topic:
        print(f"{count}: {i['Title']}")
        listNomor.append(count)
        count += 1
    nomor = int(input("Masukkan nomor topic yang ingin diupdate: "))
    if nomor in listNomor:
        print("Data eksisting....")
        print(f"Title\t\t:{list_topic[nomor-1]['Title']}")
        print(f"Description\t:{list_topic[nomor-1]['Description']}")
        print("Masukkan data baru. Jika tidak ingin diubah, kosongkan saja.")
        titleBaru = input("Masukkan Title: ")
        deskripsibaru = input("Masukkan Description: ")
        if titleBaru != '':
            list_topic[nomor-1]['Title'] = titleBaru
        else:
            pass
        if deskripsibaru != '':
            list_topic[nomor-1]['Description'] = deskripsibaru
        else:
            pass

        print("Update topic selesai")
    else:
        print("Nomor topic tidak ada")


def add_activity(list_topic, dict_activity, id_activity):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin tambah aktifitas.
    Minta data aktifitas baru, tambahkan counter id_activity dengan 1, lalu tambahkan ke dalam dict_activity.
    Tambahkan juga id_activity ke dalam list aktifitas topik.
    Tanya jika ingin menambah aktifitas lagi

    Return: id_activity yang terakhir digunakan
    '''

    print('----Fungsi "add_activity" dijalankan----')
    # jawaban anda di bawah ini


def udpate_activity(list_topic, dict_activity):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin diupdate.
    Menampilkan data activity pada topik yang dipilih, minta inputan activity.
    Minta data update ke user, jika field tidak ingin diupdate, user cukup mengosongkan field
    '''
    print('----Fungsi "update_activity" dijalankan----')
    # jawaban anda di bawah ini
    nomer = 1
    listNomer = []
    for i in list_topic:
        print(f"{nomer}: {i['Title']}")
        listNomer.append(nomer)
        nomer += 1
    nomorTopic = int(
        input("Masukkan nomor topic yang ingin diupdate activitynya: "))
    if nomorTopic in listNomer:
        print("List activity:")
        print("ID\t| Title\t\t\t| Type\t\t\t| Description")
        print("-"*80)
        for i in list_topic[nomorTopic-1]['Activities']:
            print(
                f"{i}\t| {dict_activity[i]['Title']}\t\t\t| {dict_activity[i]['Type']}\t\t\t| {dict_activity[i]['Description']}")
        pilihId = int(input("Masukkan ID Activity yang ingin diupdate: "))
        if pilihId in dict_activity:
            print("Masukkan data baru, kosongkan jika tidak ingin diupdate.")
            judulBaru = input("Masukkan Title Activity: ")
            tipeBaru = input("Masukkan Type Activity: ")
            deskripsiBaru = input("Masukkan Description Actvity: ")
            if judulBaru != '':
                dict_activity[pilihId]['Title'] = judulBaru
            if tipeBaru != '':
                dict_activity[pilihId]['Type'] = tipeBaru
            if deskripsiBaru != '':
                dict_activity[pilihId]['Description'] = deskripsiBaru
            print("Update Activity selesai.")
    else:
        print("nomor topic tidak ada")
    input("\nTekan Enter untuk kembali ke menu utama...")


def delete_activity(list_topic, dict_activity, dict_submission, dict_grade):
    '''
    Menampilkan semua topik, minta inputan topik. 
    Menampilkan data activity pada topik yang dipilih, minta inputan activity.
    Hapus activity, submission, dan grade dengan id activity yang dipilih
    '''
    print('----Fungsi "delete_activity" dijalankan----')
    # jawaban anda di bawah ini


def print_topic_to_file(list_topic, dict_activity):
    '''
    Minta nama file.
    Print setiap detail topik, beserta list aktifitasnya ke file.
    '''

    print('----Fungsi "print_topic_to_file" dijalankan----')
    # jawaban anda di bawah ini
    try:
        namaFile = open(input("Masukkan nama file: "), "x")
    except FileExistsError:
        print("Nama file tersebut sudah ada sebelumnya. Silahkan ganti nama file")
        namaFile = open(input("Masukkan nama file: "), "x")
    for i in list_topic:
        namaFile.write(f"Title\t\t: {i['Title']}\n")
        namaFile.write(f"Description\t: {i['Description']}\n")
        namaFile.write("List activity:\n")
        namaFile.write("ID\t| Title\t\t\t\t\t| Type\t\t\t| Description\n")
        namaFile.write(
            "----------------------------------------------------------------------\n")
        for j in i['Activities']:
            if len(dict_activity[j]['Title']) > 14:
                if len(dict_activity[j]['Type']) < 10:
                    namaFile.write(
                        f"{j}\t| {dict_activity[j]['Title']}\t| {dict_activity[j]['Type']}\t\t| {dict_activity[j]['Description']}\n")
                elif len(dict_activity[j]['Type']) >= 10:
                    namaFile.write(
                        f"{j}\t| {dict_activity[j]['Title']}\t| {dict_activity[j]['Type']}\t| {dict_activity[j]['Description']}\n")
            elif len(dict_activity[j]['Title']) <= 14:
                if len(dict_activity[j]['Type']) < 10:
                    namaFile.write(
                        f"{j}\t| {dict_activity[j]['Title']}\t\t| {dict_activity[j]['Type']}\t\t| {dict_activity[j]['Description']}\n")
                elif len(dict_activity[j]['Type']) >= 10:
                    namaFile.write(
                        f"{j}\t| {dict_activity[j]['Title']}\t\t| {dict_activity[j]['Type']}\t| {dict_activity[j]['Description']}\n")
        namaFile.write("\n\n")
    print("Print topic dan activity ke file berhasil")
    input("\n\nTekan Enter untuk kembali ke menu utama...")


if __name__ == "__main__":
    #type_activity = ['assignment', 'material']
    # id_activity adalah variable global untuk id unik semua activity di semua topic
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
