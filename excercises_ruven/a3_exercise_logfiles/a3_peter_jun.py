import re


def logtolist(file):
    """
    takes a log file and returns a list of dicts containing logs
    """
    return [line_to_dict(line) for line in file]


def line_to_dict(line):
    """
    Takes a string filters and returns a dict with wanted key-value pairs-
    """
    data_dict = {}
    search_ip_address = re.search(r"(\d*\.){3}\d*", line)
    ip_adress = search_ip_address.group() if search_ip_address else 'No IP address found'
    search_timestamp = re.search(r"\[(.*)]", line)
    timestamp = search_timestamp.group(1) if search_timestamp else 'No timestamp found'
    search_request = re.search("GET.*HTTP/.{3}", line)
    request = search_request.group() if search_request else 'No request found'
    data_dict["ip_address"] = ip_adress
    data_dict["timestamp"] = timestamp
    data_dict["request"] = request
    return data_dict


def re_logtolist(file):
    return logtolist(file)


if __name__ == '__main__':
    f = open("a3_access_log_file/mini-access-log.txt")
    full_logs_lst = logtolist(f)
    print(full_logs_lst)
