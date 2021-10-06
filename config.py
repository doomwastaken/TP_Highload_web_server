def read_config(filename: str) -> (int, str):
    cpu_limit = 6
    document_root = "/home/vk/tp/TP_Highload_web_server"
    with open(filename, "r") as config_file:
        for line in config_file:
            split_line = line.split(" ")
            if split_line[0] == "cpu_limit":
                cpu_limit = int(split_line[1])

            if split_line[0] == "document_root":
                document_root = split_line[1].rstrip("\n")

    return cpu_limit, document_root


HOST = "0.0.0.0"
PORT = 80
CONFIG_FILE = "/home/vk/tp/TP_Highload_web_server/httpd.conf"

CPU_LIMIT, DOCUMENT_ROOT = read_config(CONFIG_FILE)
