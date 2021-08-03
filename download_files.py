import os
import TCGA_Download.download as dw

def get_files_names(flist):
    return [file.rstrip() for file in open(flist, 'r')]

output_dir = '/Users/n10337547/Projects/1_Data/Normal_redownload'
files_list = '/Users/n10337547/Projects/download/files.txt'
filenames = get_files_names(files_list)

dw.download_files_by_file_names(filenames, output_dir)
