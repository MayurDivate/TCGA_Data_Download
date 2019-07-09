import TCGA_Download.api_end_points as api
import TCGA_Download.search as query
from TCGA_Download.rnaseq import RNAseq

# RNAseq data in TCGA

# fields = ['file_name','data_type', 'data_format', 'type']

fields = ['file_name']

rnaseq_obj = RNAseq(fields)

wtype = query.get_filter('=', 'analysis.workflow_type','HTSeq - FPKM')


filters = query.add_filter(rnaseq_obj.get_filters(), wtype)


rnaseq_obj.filters = filters



rnaseq_query = query.Query(api.get_files_ep(), rnaseq_obj.get_params(size=2))

print('page 1')
js_res = rnaseq_query.get_response()
query.print_hits(query.get_hits(js_res))

