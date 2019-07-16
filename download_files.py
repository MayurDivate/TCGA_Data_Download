

import TCGA_Download.download as dw

files_list = '/Users/mayurdivate/QUT/Work/Projects/1_CUP/FPKM_txt/files.txt'

def get_files_names(flist):
    filenames = []

    with open(files_list,'r') as f:
        for line in f:
            line = line.rstrip()
            filenames.append(line)
    return filenames

filenames = get_files_names(files_list)

output_dir = '/Users/mayurdivate/QUT/Work/Projects/1_CUP/FPKM_txt'

dw.download_files_by_file_names(filenames, output_dir)
