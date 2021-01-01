import os
class MainSorting():
    """ Create Main Class """
    def start(self):
        self.check_old_symb() # TODO need testing
        self.check_empty_dirs() # TODO need testing
        """ Geting cortage and send to backend """
        for lines in os.walk(self.src_dir):
            self.counter.append(lines)
        for pwd, dirs, files in self.counter:
            for file in files:
                if self.prefix in file and self.src_dir != pwd or self.src_dir == pwd:
                    #print(file) # DEBUG
                    self.parse_serial_name(file, pwd)
    def check_dir(self, input_dir):
        """ Input path to dir, and check it """
        if os.path.isdir(input_dir) != True:
            os.mkdir(input_dir) # COMMENT THIS FOR TESTINGI
            print("Dir: "+input_dir+" has been added")
    def check_symb(self, src, dst):
        """ Inputing for create symbolic link """
        if os.path.exists(dst) != True:
            os.symlink(src, dst) # COMMENT THIS FOR TESTING
            print("Created: "+dst)
    def check_old_symb(self):
        """ Checking oldest symlink when target deleted """
        for lines in os.walk(self.dst_dir):
            self.count.append(lines)
        for pwd, dirs, files in self.count:
            for file in files:
                symb_file = (pwd+'/'+file)
                trg_file = os.readlink(symb_file)
                if os.path.exists(trg_file) != True:
                    os.remove(symb_file) # COMMENT THIS FOR TESTING
                    print("File "+symb_file+" has beed deleted")
    def check_empty_dirs(self):
        for liness in os.walk(self.dst_dir):
            self.count_dir.append(liness)
        for pwd, dirs, files in self.count_dir:
            for dir in dirs:
                dir_trgt = (pwd+'/'+dir)
                if not os.listdir(dir_trgt) :
                    print(f"Directory {dir_trgt} has been deleted")
                    os.rmdir(dir_trgt) # COMMENT THIS FOR TESTING
#----------------------------------------------------------#


class LostFilm(MainSorting):
    """ Create LostFilm Class """
    def __init__(self, prefix, src_dir, dst_dir):
        """ Init main metod """
        self.prefix = prefix
        self.src_dir = src_dir
        self.dst_dir = dst_dir
        self.counter, self.count, self.count_dir = [], [], []
    def parse_serial_name(self, input_file, input_pwd):
        """ Inputing and parsing str src and dst file, and dst dirs """ 
        file_ext = ".LostFilm.TV.mkv"
        season_num = input_file[0:-25] [-7:-1] + file_ext # split str to "S01E01" and add ".LostFilm.TV.mkv"
        dir_name = input_file[0:-33] # split str to "Happy"
        src = input_pwd + '/' + input_file
        dst = self.dst_dir + '/' + dir_name + '/' + season_num
        dst_dirname = self.dst_dir + '/' + dir_name
        self.check_dir(self.dst_dir)
        self.check_dir(dst_dirname)
        self.check_symb(src, dst)
#--------------------------------------------------------------------
