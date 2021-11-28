import logging
import yaml
from django.shortcuts import render
from .utils import calculate_number_of_records


def index(request):
    template = 'index.html'

    # reading config file
    with open("config.yaml", "r") as stream:
        try:
            config_file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)

    newyork_records_count = calculate_number_of_records(config_file['newyork_times']['connection_string'],
                                                        config_file['newyork_times']['database_name'],
                                                        config_file['newyork_times']['collection_name'])

    cnbc_records_count = calculate_number_of_records(config_file['cnbc']['connection_string'],
                                                     config_file['cnbc']['database_name'],
                                                     config_file['cnbc']['collection_name'])

    total_records = newyork_records_count + cnbc_records_count

    context = {
        "newyork_times_records": newyork_records_count,
        "cnbc_records": cnbc_records_count,
        "total_records": total_records
    }

    return render(request, template, context)
