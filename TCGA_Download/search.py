import requests
import json

class Query:
    def __init__(self, endpoint, params):
        self.endpoint = endpoint
        # self.fields = fields
        self.params = params
        self.size = params['size']

    def get_headers(self, response):
        return response.headers

    def get_response(self):
        response = requests.get(self.endpoint, params=self.params).json()
        return response

    def get_next_page_response(self):
        self.params['from'] = self.params['from'] + self.params['size']
        return self.get_response()

    def get_previous_page_response(self):
        if self.params['from'] - self.params['size'] < 0:
            self.current_start = 0
        else:
            self.params['from'] = self.params['from'] - self.params['size']

        return self.get_response()

def add_filter(filters, new_filter):

    filters['content'].append(dict(new_filter))
    return filters


def get_filter(op, field, value):
    my_filter = {
        'op': op,
        'content': {
            'field': field,
            'value': value
        }
    }
    return my_filter


def get_json_response(response):
    return response.json()


def get_data(js_response):
    return js_response['data']


def get_hits(js_response):
    return js_response['data']['hits']


def get_pagination(js_response):
    return js_response['data']['pagination']


def get_number_pages(js_response):
    return get_pagination(js_response)['pages']


def get_current_page(js_response):
    return get_pagination(js_response)['page']


def get_total_results(js_response):
    return get_pagination(js_response)['total']


def get_warnings(js_response):
    return get_data(js_response)['warnings']


def print_hits(hits):
    for h in hits:
        print(h)
