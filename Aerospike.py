import aerospike
from aerospike import exception as ex
from aerospike_helpers.operations import operations as op_helpers
from pprint import pprint
from School import School
import csv


class Aerospike:
    def __init__(self, namespace: str, set_name: str):
        self.config = {'hosts': [('127.0.0.1', 3000)]}
        self.client = aerospike.client(self.config).connect()
        self.namespace = namespace
        self.set_name = set_name

    def import_datas(self):
        with open("data/db_to_import.csv", 'r') as fichier:
            csv_reader = csv.reader(fichier)
            next(csv_reader)  # Ignore the first line
            key = 1
            for row in csv_reader:
                bins = {
                    "title": row[0],
                    "name": row[1],
                    "address": row[2],
                    "real_address": row[3],
                    "department": row[4],
                    "country": row[5],
                    "tel": row[6],
                    "email": row[7]
                }
                self.create(key=key, bins=bins)
                key = key + 1

    def create(self, key: int, bins: dict):
        # Creation of all key
        full_key = (self.namespace, self.set_name, key)

        write_policy = {'key': aerospike.POLICY_KEY_SEND}
        try:
            # Write bins
            self.client.put(full_key, bins, policy=write_policy)
            print('Création réussie  -  Clé: ', key)

        except ex.AerospikeError as e:
            print("Échec de la création\nErreur: {0} [{1}]".format(e.msg, e.code))

    def close_client(self):
        self.client.close()

    def retrieve_one_record(self, key):
        try:
            (key_, meta, bins) = self.client.get(key)
            print('Clé:', key[2], '\nEnregistrement:')
            pprint(bins)
        except ex.AerospikeError as e:
            print("Erreur: {0} [{1}]".format(e.msg, e.code))

    def retrieve_all_records(self) -> list:
        schools = []
        try:
            query = self.client.query(self.namespace, self.set_name)
            records = query.results()
            sorted_records = sorted(records, key=lambda r: r[0][2])

            for result in sorted_records:
                school = self.transform_in_object_school(entry=result)
                schools.append(school)

            return schools

        except aerospike.exception.AerospikeError as e:
            print("Erreur: {0} [{1}]".format(e.msg, e.code))

    def update_record(self, key, bins):
        try:
            self.client.put(key, bins)
            print("Enregistrement mis à jour avec succès.")
        except aerospike.exception.AerospikeError as e:
            print("Erreur: {0} [{1}]".format(e.msg, e.code))

    def delete_record(self, key):
        full_key = (self.namespace, self.set_name, key)
        try:
            self.client.remove(full_key)
            print("Enregistrement supprimé avec succès.")
        except aerospike.exception.AerospikeError as e:
            print("Erreur: {0} [{1}]".format(e.msg, e.code))

    def transform_in_object_school(self, entry: tuple) -> School:
        bins = entry[2]
        return School(id=entry[0][2], department=bins.get("department"), real_address=bins.get("real_address"),
                      address=bins.get("address"), tel=bins.get("tel"), country=bins.get("country"),
                      title=bins.get("title"), name=bins.get("name"), email=bins.get("email"))
