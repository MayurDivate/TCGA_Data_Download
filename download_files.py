

import TCGA_Download.download as dw

<<<<<<< HEAD
files_list = '/Users/mayurdivate/QUT/Work/Projects/NBL.txt'
#flist = [file.rstrip() for file in open(files_list,'r')]

def get_files_names(flist):
    filenames = []
=======
files_list = '/Users/mayurdivate/QUT/Work/Projects/1_CUP/FPKM_txt/files.txt'

def get_files_names(flist):
    filenames = []

>>>>>>> dd12018cf7028fa025e9b61e7136c2b646cc284d
    with open(files_list,'r') as f:
        for line in f:
            line = line.rstrip()
            filenames.append(line)
    return filenames

filenames = get_files_names(files_list)

<<<<<<< HEAD
output_dir = '/Users/mayurdivate/QUT/Work/Projects/NBL'
=======
output_dir = '/Users/mayurdivate/QUT/Work/Projects/1_CUP/FPKM_txt'
>>>>>>> dd12018cf7028fa025e9b61e7136c2b646cc284d

dw.download_files_by_file_names(filenames, output_dir)
