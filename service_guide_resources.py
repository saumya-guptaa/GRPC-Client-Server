import json

import total_pb2


def read_service_guide_database():
    service_list = []
    with open("service_guide_db.json") as service_guide_db_file:
        for item in json.load(service_guide_db_file):
            service_add = total_pb2.service_add(
                name=item["name"],
                address=item["location"]["address"],
                port=item["location"]["port"])
            service_list.append(service_add)
    return service_list
