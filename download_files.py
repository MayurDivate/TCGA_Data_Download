import TCGA_Download.download as dw

files_list = '/Users/n10337547/GitHub/TCGA_Data_Download/TCGA_Download/normal_download_sample_id.txt'

def get_files_names(flist):
    return [file.rstrip() for file in open(flist, 'r')]

filenames = get_files_names(files_list)

output_dir = '/Users/n10337547/Projects/1_Data/Normal_redownload'

dw.download_files_by_file_names(filenames, output_dir)
