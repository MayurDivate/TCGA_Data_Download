import json as js
import pandas as pd

class RNAseq:
    default_fields = [
        'file_name',
        #'project_id',
        'cases.primary_site',
        'cases.project.project_id',
        'cases.disease_type',
        'cases.diagnoses.tissue_or_organ_of_origin',
        'cases.diagnoses.tumor_stage',
        'cases.diagnoses.primary_diagnosis',
        'cases.project.dbgap_accession_number',
        'cases.project.program.name',
        'cases.samples.sample_type',
        'cases.samples.tissue_type',
        'cases.samples.sample_id',
        'cases.samples.composition',
        'cases.demographic.gender',
        'cases.demographic.ethnicity',

    ]

    # default_expand = 'cases.samples,cases.project,cases.project.program'

    def __init__(self, outfile='test_tcga_rnaseq.tsv', fields=None, expand='cases.diagnoses'):

        if fields is None:
            self.fields = self.default_fields
        else:
            self.fields = fields

        self.expand = expand
        self.filters = self.get_filters()
        self.params = self.get_params()
        self.outfile = outfile

    def get_filters(self):
        filters = {
            "op": "and",
            "content": [
                {
                    "op": "=",
                    "content": {
                        "field": "data_category",
                        "value": "Transcriptome Profiling"
                    }
                },
                {
                    "op": "=",
                    "content": {
                        "field": "experimental_strategy",
                        "value": "RNA-Seq"
                    }
                }
                # adding filter to fetch only metadata of following file
                # ,{
                #     "op": "=",
                #     "content": {
                #         "field": "file_name",
                #         "value": "d1489e83-a47f-4d2e-b330-c0698b1ccc27.htseq.counts.gz"
                #     }
                #}

            ]

        }

        return filters

    def get_fields(self):
        return ','.join(self.fields)

    def get_params(self, start_from=0, size=10):

        params = {
            'filters': js.dumps(self.filters),
            'fields': self.get_fields(),
            'format': 'JSON',
            'size': size,
            'pretty': 'true',
            'expand': self.expand,
            'from': start_from
        }

        return params

    def get_value_of_dict_key(self, dictX, keyX):
        """
        :param dictX:
        :param keyX:
        :return: it returns "None" string if key does not exist
        """

        if keyX in dictX:
            return dictX[keyX]
        else:
            return 'None'

    def get_filename(self, hit):
        return self.get_value_of_dict_key(hit, 'file_name')

    def get_id(self, hit):
        return self.get_value_of_dict_key(hit, 'id')

    def get_cases_dict(self, hit):
        return self.get_value_of_dict_key(hit, 'cases')[0]

    def get_sample_dict(self, hit):
        return self.get_value_of_dict_key(self.get_cases_dict(hit), 'samples')[0]

    def get_diagnoses_dict(self, hit):
        return self.get_value_of_dict_key(self.get_cases_dict(hit), 'diagnoses')[0]

    def get_tissue_or_organ_of_origin(self, hit):
        return self.get_value_of_dict_key(self.get_diagnoses_dict(hit), 'tissue_or_organ_of_origin')

    def get_primary_diagnosis(self, hit):
        return self.get_value_of_dict_key(self.get_diagnoses_dict(hit), 'primary_diagnosis')

    def get_tumor_stage(self, hit):
        return self.get_value_of_dict_key(self.get_diagnoses_dict(hit), 'tumor_stage')

    def get_demographic_dict(self, hit):
        return self.get_value_of_dict_key(self.get_cases_dict(hit), 'demographic')

    def get_gender(self, hit):
        return self.get_value_of_dict_key(self.get_demographic_dict(hit), 'gender')

    def get_ethnicity(self, hit):
        return self.get_value_of_dict_key(self.get_demographic_dict(hit), 'ethnicity')

    def get_project_dict(self, hit):
        return self.get_value_of_dict_key(self.get_cases_dict(hit), 'project')

    def get_program_dict(self, hit):
        return self.get_value_of_dict_key(self.get_project_dict(hit), 'program')

    def get_program_name(self, hit):
        return self.get_value_of_dict_key(self.get_program_dict(hit), 'name')

    def get_dbgap_accession_number(self, hit):
        return self.get_value_of_dict_key(self.get_project_dict(hit), 'dbgap_accession_number')

    def get_project_id(self, hit):
        return self.get_value_of_dict_key(self.get_project_dict(hit), 'project_id')

    def get_disease_type(self, hit):
        return self.get_value_of_dict_key(self.get_cases_dict(hit), 'disease_type')

    def get_submitter_id(self, hit):
        return self.get_value_of_dict_key(self.get_cases_dict(hit), 'submitter_id')

    def get_primary_site(self, hit):
        return self.get_value_of_dict_key(self.get_cases_dict(hit), 'primary_site')

    def get_tissue_type(self, hit):
        return self.get_value_of_dict_key(self.get_sample_dict(hit), 'tissue_type')

    def get_composition(self, hit):
        return self.get_value_of_dict_key(self.get_sample_dict(hit), 'composition')

    def get_sample_type(self, hit):
        return self.get_value_of_dict_key(self.get_sample_dict(hit), 'sample_type')

    def get_sample_id(self, hit):
        return self.get_value_of_dict_key(self.get_sample_dict(hit), 'sample_id')

    def get_site_of_resection_or_biopsy(self, hit):
        return self.get_value_of_dict_key(self.get_diagnoses_dict(hit), 'site_of_resection_or_biopsy')

    def get_tumor_grade(self, hit):
        return self.get_value_of_dict_key(self.get_diagnoses_dict(hit), 'tumor_grade')

    def get_tissue_or_organ_of_origin(self,hit):
        return self.get_value_of_dict_key(self.get_diagnoses_dict(hit), 'tissue_or_organ_of_origin')

    def json_to_dataframe(self, hits):

        index = ['filename', 'submitter_id', 'project_id', 'tissue_type', 'primary_diagnosis',
                 'tumor_stage', 'disease_type', 'gender', 'ethnicity',
                 'program_name', 'dbgap_accession_number', 'primary_site', 'tissue_or_organ_of_origin',
                 'composition', 'sample_type', 'site_of_resection_or_biopsy','tumor_grade',
                 'sample_id', 'id']

        rnaseq_df = None

        for hit in hits:

            outfields = [self.get_filename(hit), self.get_submitter_id(hit),
                         self.get_project_id(hit), self.get_tissue_type(hit),
                         self.get_primary_diagnosis(hit), self.get_tumor_stage(hit),
                         self.get_disease_type(hit), self.get_gender(hit),
                         self.get_ethnicity(hit), self.get_program_name(hit),
                         self.get_dbgap_accession_number(hit), self.get_primary_site(hit),
                         self.get_tissue_or_organ_of_origin(hit),
                         self.get_composition(hit), self.get_sample_type(hit),
                         self.get_site_of_resection_or_biopsy(hit), self.get_tumor_grade(hit),
                         self.get_sample_id(hit), self.get_id(hit)]

            df = pd.DataFrame(outfields, index=index).T

            if rnaseq_df is None:
                rnaseq_df = df
            else:
                rnaseq_df = rnaseq_df.append(df)

        return rnaseq_df

    def dump_df_to_file(self, df, empty_the_file=False):

        if empty_the_file:
            open(self.outfile, 'w').close()
            df.to_csv(self.outfile, sep='\t', index=False)

        else:
            with open(self.outfile, 'a+') as f:
                df.to_csv(f, sep='\t', index=False, header=False)
