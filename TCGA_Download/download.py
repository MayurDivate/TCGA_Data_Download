import json as js
import os
import re as regx

import requests

import TCGA_Download.api_end_points as api
from TCGA_Download.files import TCGA_File


def download_files_by_file_names(file_names, outputdir=".", chunksize=50):
    ids = []
    print("Getting file ids")
    for name in file_names:
        file_id = TCGA_File(name).get_file_id_from_name()
        ids.append(file_id)

    llen = len(ids)
    print(llen)
    start = 0
    end = chunksize

    while start < llen:
        print("Chunk from ", start, " to ", llen)
        if end > llen:
            chunk_ids = ids[start:]
            download_files(chunk_ids, outputdir)
            break

        chunk_ids = ids[start: end]
        download_files(chunk_ids, outputdir)

        start = end
        end += chunksize


def download_files(ids, outdir):
    params = {"ids": ids}

    response = requests.post(api.get_data_ep(),
                             data=js.dumps(params),
                             headers={"Content-Type": "application/json"}
                             )

    response_head_cd = response.headers["Content-Disposition"]
    print(response_head_cd)

    file_name = regx.findall("filename=(.+)", response_head_cd)[0]
    file_name = os.path.join(outdir, file_name)

    with open(file_name, "wb") as output_file:
        print("output_file = ", file_name)
        output_file.write(response.content)
