import os
import TCGA_Download.download as dw

dirx = '/Users/mayurdivate/QUT/WFH/TCGA_Labelling/TCGA_data_download'

files_list = os.path.join(dirx, 'redownload_files.txt')

def get_files_names(files_list):
    return [file.rstrip() for file in open(files_list, 'r')]


filenames = get_files_names(files_list)

output_dir = os.path.join(dirx, 'TCGA_re')

dw.download_files_by_file_names(filenames, output_dir)
