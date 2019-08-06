# coding=utf-8
import ftplib


class Ftp:
    def __init__(self, host_, user_name, pass_word):
        self.host_ = host_
        self.user_name = user_name
        self.pass_word = pass_word
        self.f = ftplib.FTP(host_)
        self.f_l = self.f.login(self.user_name, self.pass_word)

    def pwd_path(self):
        # 获取当前路径
        return self.f.pwd()

    def ftp_download(self):
        # 下载文件
        # 下载目标文件的名称
        file_remote = '1.txt'
        # 下载到本地文件
        file_local = 'D:\\test_data\\ftp_download.txt'
        bufsize = 1024  # 设置缓冲器大小
        fp = open(file_local, 'wb')
        self.f.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
        fp.close()

    def ftp_upload(self):
        # 上传文件
        '''以二进制形式上传文件'''
        file_remote = 'ftp_upload.txt'
        file_local = 'D:\\test_data\\ftp_upload.txt'
        bufsize = 1024  # 设置缓冲器大小
        fp = open(file_local, 'rb')
        self.f.storbinary('STOR ' + file_remote, fp, bufsize)
        fp.close()

    def quit(self):
        # 断开连接
        self.f.quit()
        return "断开连接"
