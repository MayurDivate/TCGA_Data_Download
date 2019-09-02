import json as js

import TCGA_Download.api_end_points as api
from TCGA_Download.search import Query


class Projects:
    def __init__(self, fields):
        self.fields = fields

    def get_all_projects_details(self):
        params = {
            "fields": self.fields,
            "format": "JSON",
            "size": 1000
        }

        project_info = js.loads(Query(api.get_projects_ep(), params).get_json_response())
        self.parse_project_info(project_info)


    def parse_project_info(self, pinfo):
        """
        data
            hits[]

            pagination

        warnings
        """

        print("Total projects: ",len(pinfo['data']['hits']))

        print(pinfo['data']['hits'][0])
        #print(pinfo['warnings'])
