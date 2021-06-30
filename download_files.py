<<<<<<< HEAD
import os
import TCGA_Download.download as dw

dirx = '/Users/mayurdivate/QUT/WFH/TCGA_Labelling/TCGA_data_download'

files_list = os.path.join(dirx, 'redownload_files.txt')
=======
import TCGA_Download.download as dw

files_list = '/Users/n10337547/Projects/download/files.txt'
>>>>>>> f988b03a7e3d9335b793c42d14103c535c2199da

def get_files_names(files_list):
    return [file.rstrip() for file in open(files_list, 'r')]

filenames = get_files_names(files_list)

<<<<<<< HEAD
output_dir = os.path.join(dirx, 'TCGA_re')
=======
output_dir = '/Users/n10337547/Projects/download/'
>>>>>>> f988b03a7e3d9335b793c42d14103c535c2199da

dw.download_files_by_file_names(filenames, output_dir)
