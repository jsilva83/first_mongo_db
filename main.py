# Import external modules.
import pymongo


def main():
    password = input('Enter your password for MongoDB:\n')
    # Connect to Mongo cluster.
    client = pymongo.MongoClient(
        f"mongodb+srv://jsilva_admin:{password}"
        "@jhscluster.zzi65.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    )
    # # Creates a test database.
    # db = client['test']
    # print(client.list_database_names())
    # # Create a collection.
    # col = db['customers']
    # print(db.list_collection_names())
    # # Insert data.
    # record = {
    #     'name': 'RUMOS',
    #     'address': 'Campo Grande, Lisboa',
    # }
    # a_record = col.insert_one(record)
    # print(a_record.inserted_id)
    # records = [
    #     {
    #         'name': 'RUMOS Porto',
    #         'address': 'Porto',
    #     },
    #     {
    #         'name': 'INFARMED',
    #         'address': 'Lisboa'
    #     },
    # ]
    # a_set_records = col.insert_many(records)
    # print(a_set_records.inserted_ids)
    # Print all records.
    db = client['test']
    col = db['customers']
    for x in col.find():
        print(x)
    # Query if address is Lisboa.
    myquery = {"address": "Lisboa"}
    for x in col.find(myquery):
        print(x)
    # Query if the address contains Lisboa.
    myquery = {"address": {"$regex": "Lisboa"}}
    for x in col.find(myquery):
        print(x)
    # Delete records.
    myquery = {"address": {"$regex": "^S"}}
    x = col.delete_many(myquery)
    print(f'{x.deleted_count} records deleted.')
    # Update records.
    myquery = {"address": 'Campo Grande, Lisboa'}
    new_values = {"$set": {"address": 'Campo Grande 6, Lisboa'}}
    col.update_one(myquery, new_values)
    for x in col.find():
        print(x)
    # Return a smaller number of records.
    my_result = col.find().limit(2)
    print('limited results')
    for x in my_result:
        print(x)
    pass
    return


if __name__ == '__main__':
    main()
