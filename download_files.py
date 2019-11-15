import TCGA_Download.download as dw

files_list = '/Users/n10337547/Projects/download/files.txt'

def get_files_names(flist):
    return [file.rstrip() for file in open(files_list, 'r')]

filenames = get_files_names(files_list)

output_dir = '/Users/n10337547/Projects/download/'

dw.download_files_by_file_names(filenames, output_dir)
