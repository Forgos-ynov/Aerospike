from Aerospike import Aerospike

aerospike = Aerospike(namespace="test", set_name="school")

bins = {
    'nom': 'Donald',
    'prenom': 'John',
    'age': 30
}


# aerospike.import_datas()

# aerospike.create(key=3001, bins=bins)
# aerospike.update_record(key=key, bins=bins)
# aerospike.delete_record(key=1)
# record = aerospike.retrieve_one_record(key=key)
records = aerospike.retrieve_all_records()




aerospike.close_client()
alpha = 1


