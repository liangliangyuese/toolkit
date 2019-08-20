# coding=utf-8
import ftplib


class Ftp:
    def __init__(self, host, user_name, pass_word):
        self.host_ = host
        self.user_name = user_name
        self.pass_word = pass_word
        self.f = ftplib.FTP(host)
        self.f_l = self.f.login(self.user_name, self.pass_word)

    def pwd_path(self):
        # 获取当前路径
        return self.f.pwd()

    def ftp_download(self, file_remote=None, file_local=None):
        # file_remote 下载目标文件地址
        # file_local  下载到本地的地址
        if file_remote and file_local:
            buffer_size = 1024  # 设置缓冲器大小
            fp = open(file_local, 'wb')
            self.f.retrbinary('RETR %s' % file_remote, fp.write, buffer_size)
            fp.close()
        else:
            raise ValueError("不存在目标参数")

    def ftp_upload(self, file_remote=None, file_local=None):
        # file_remote 下载目标文件地址
        # file_local  下载到本地的地址
        if file_remote and file_local:
            buffer_size = 1024  # 设置缓冲器大小
            fp = open(file_local, 'rb')
            self.f.storbinary('STOR ' + file_remote, fp, buffer_size)
            fp.close()
        else:
            raise ValueError("不存在目标参数")

    def quit(self):
        # 断开连接
        self.f.quit()
        return "ftp 连接已断开"
