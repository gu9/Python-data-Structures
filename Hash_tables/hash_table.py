# Standard implementation of Hash table in Python

hash_table = [[] for _ in range(10)]
print (hash_table)


def delete(hash_table, key):
    """
    Deleting elements from hash table
    :param hash_table: Given hash table
    :param key: input by user
    :return: None
    """
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break

    if key_exists:
        del bucket[i]
        print ('Key {} deleted'.format(key))
    else:
        print ('Key {} not found'.format(key))


def insert(hash_table, key, value):
    """
    This function takes user input and assign a bucket to it using Chaining
    :param hash_table:
    :param key:
    :param value:
    :return:
    """

    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))


insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
insert(hash_table, 11, 'Nepal')
insert(hash_table, 253, 'USA')
insert(hash_table, 220, 'India')
insert(hash_table, 120, 'Nepal')
insert(hash_table, 225, 'USA')
insert(hash_table, 250, 'India')
print (hash_table)