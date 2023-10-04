class Change_Name_Interface:
    def __init__(self, mikrotik_connection):
        self.connection = mikrotik_connection

    def change_interface_name(self, interface, new_name):
        try:
            command = f'/interface set {interface} name={new_name}'
            stdin, stdout, stderr = self.connection.exec_command(command)
            error = stderr.read().decode()
            if not error:
                print("Nama Interface berhasil diganti")
            else:
                print("Terjadi kesalahan:",error)
        except Exception as e:
            print("Terjadi Kesalahan:",str(e))
