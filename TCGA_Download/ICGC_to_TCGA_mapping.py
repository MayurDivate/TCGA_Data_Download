import TCGA_Download.api_end_points as ep
import pandas as pd
import json
import TCGA_Download.search as sh


# Search parameters
# filter results using following criteria
filterx = {'op': '=', 'content': {'field': 'data_type', 'value': ["Gene Expression Quantification"]}}

# retrive following fields
fieldx = ["file_id,file_name",
         "cases.case_id,data_type",
         "cases.samples.sample_id",
         "cases.samples.portions.analytes.aliquots.aliquot_id",
         "cases.samples.portions.analytes.aliquots.submitter_id"]

# build search paramters using filterx and fieldx
def get_params(start_from=0, size=100):
    paramsx = {
        'filters':  json.dumps(filterx),
        'fields': ",".join(fieldx),
        'from': start_from,
        'size': size
    }

    return paramsx

#response = requests.get(ep.get_files_ep(), params= paramsx)
#print(json.dumps(response.json(), indent=2))


# json >>>  dict >>> dataframe
def get_dataframe_from_json_response(resx):
    frames = []
    for res in resx:
        dx= {'id': res['id'],
        'case_id': res['cases'][0]['case_id'],
        'sample_id': res['cases'][0]["samples"][0]["sample_id"],
        'aliquot_id': res['cases'][0]["samples"][0]['portions'][0]['analytes'][0]['aliquots'][0]['aliquot_id'],
        'filename': res['file_name'],
        'file_id': res['file_id'],
        'data_type': res['data_type']}

        df = pd.DataFrame(dx, index=[1])
        frames.append(df)
    return frames

icgc_query = sh.Query(ep.get_files_ep(), params=get_params())
js_res = icgc_query.get_response()
print(sh.get_pagination(js_res))

total_pages = sh.get_number_pages(js_res)

# first page
print('page number: ', sh.get_current_page_number(js_res))
dataframes = get_dataframe_from_json_response(sh.get_hits(js_res))
outdf = pd.concat(dataframes)


# page 2 to page last page
for page in range(total_pages - 1):
    js_res = icgc_query.get_next_page_response()
    print('page number: ', sh.get_current_page_number(js_res))
    dfx = get_dataframe_from_json_response(sh.get_hits(js_res))
    dfx = pd.concat(dfx)
    outdf = pd.concat([outdf, dfx])


outdf.to_csv('ICGC_to_TCGA.csv', index=False)



#rnaseq_obj.dump_df_to_file(df, True)



