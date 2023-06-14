from Aerospike import Aerospike

aerospike = Aerospike(namespace="test", set_name="school")


aerospike.import_datas()

# Comme c'est du clé valeur tu n'auras pas besoin d'autres requête que celle çi
# Malhereusement comme c'est du clé valeur c'est tu récupère toutes les valeurs et tu les tries avec un script
records = aerospike.retrieve_all_records()




aerospike.close_client()


