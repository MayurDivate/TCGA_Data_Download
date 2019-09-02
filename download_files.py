

import TCGA_Download.download as dw


files_list = '/Users/mayurdivate/QUT/Work/Projects/NBL.txt'

def get_files_names(flist):
    return [file.rstrip() for file in open(files_list, 'r')]


filenames = get_files_names(files_list)

output_dir = '/Users/mayurdivate/QUT/Work/Projects/1_CUP/FPKM_txt'

dw.download_files_by_file_names(filenames, output_dir)
