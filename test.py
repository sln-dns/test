def group(id):
    id = str(id)
    id_int = list(map(int, id))
    sum_of_digits = 0
    sum_of_digits = sum(id_int)
    
    return sum_of_digits



def group_customers(n_customers):
    dict = {}
    max_key = group(n_customers)
    for i in range (0, max_key):
        dict[i] = 0
    for i in range (0, max_key):
        dict[i] = group(i)
        
    return dict

def custom_group_customers(n_first_id, n_customers):
    dict = {}
    max_key = group(n_customers)
    for i in range (0, max_key):
        dict[i] = 0
    for i in range (n_first_id, max_key):
        dict[i] = group(i)
        
    return dict






