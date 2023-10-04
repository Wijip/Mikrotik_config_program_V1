import paramiko

class MikrotikConnection:
    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.ssh_client = None

    def connect(self):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.load_system_host_keys()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(self.hostname, username=self.username, password=self.password)
            print("Login Berhasil!!")
            return True
        except paramiko.AuthenticationException:
            print("Login Gagal. Username atau password salah.")
        except paramiko.SSHException as e:
            print("Terjadi kesalahan pada koneksi SSH",str(e))
        except Exception as e:
            print("Terjadi kesalahan",str(e))

    def execute_command(self, command):
        if self.ssh_client:
            atdin, stdout, stderr = self.ssh_client.exec_command(command)
            return stdout.read().decode()
        else:
            print("Koneksi belum terbuka. silahkan login terlebih dahulu")
            return ""

    def close_connection(self):
        if self.ssh_client:
            self.ssh_client.close()
