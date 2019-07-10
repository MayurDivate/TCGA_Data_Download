# TCGA_Data_Download

This package provides utility to download data and meta-data from TCGA using its API.

#### Examples

##### rnaseq_metadata_for_fpkm_files.py

This python program download RNAseq metadata and process it page by page.
It limits max records per page to 100.
Results will be save in the tcga_rnaseq.tsv file by default.
To change default file, pas the file path with 'outfile' parameter while creating RNAseq class object.


## TCGA API documentation 

[Available fields](https://docs.gdc.cancer.gov/API/Users_Guide/Appendix_A_Available_Fields/)

[User Guide](https://docs.gdc.cancer.gov/API/Users_Guide/Search_and_Retrieval/)
