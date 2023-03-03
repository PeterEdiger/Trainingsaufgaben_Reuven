import re


def line_to_dict(line):
    search_ip_address = re.search('(\d+\.){3}\d+', line)
    ip_address = search_ip_address.group() if search_ip_address else 'No IP address found'

    search_timestamp = re.search('\[.*?]', line)
    timestamp = search_timestamp.group()[1:-1] if search_timestamp else 'No timestamp found'

    search_request = re.search(r'\".*?\"', line)
    request = search_request.group()[1:-1] if search_request else 'No request found'

    return {'ip_address': ip_address, 'timestamp': timestamp, 'request': request}


def logtolist(file):
    # with open(file_name) as file:
    lines = file.readlines()

    dict_list = [line_to_dict(line) for line in lines]

    return dict_list


def re_logtolist(file_name):
    return logtolist(file_name)
