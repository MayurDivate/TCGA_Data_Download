import TCGA_Download.download as dw
import os


def get_files_names(flist):
    return [file.rstrip() for file in open(flist, 'r')]


rdir = '/Users/n10337547/Projects/1_Data/TCGA_Htseq_count/'
files_list = [os.path.join(rdir, fx) for fx in os.listdir(rdir) if fx.startswith('count')]

for fx in files_list:
    print(">>> ", fx)
    filenames = get_files_names(fx)
    output_dir = '/Users/n10337547/Projects/1_Data/TCGA_Htseq_count/downloaded'
    dw.download_files(filenames, output_dir)
