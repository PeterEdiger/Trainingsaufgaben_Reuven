import re


def logtolist(file):
    logs_info_lst = []
    lines = file.readlines()
    for line in lines:
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

        logs_info_lst.append(data_dict)

    return logs_info_lst


def re_logtolist(file):
    return logtolist(file)


if __name__ == '__main__':
    f = open("a3_access_log_file/mini-access-log.txt")
    full_logs_lst = logtolist(f)
    print(full_logs_lst)
