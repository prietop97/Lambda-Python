def get_indices_of_item_weights(weights, length, limit):
    my_hash = {}
    for i in range(len(weights)):
        current_weight = weights[i]
        if current_weight not in my_hash:
            my_hash[limit - current_weight] = i
        else:
            return [i, my_hash[current_weight]]

    return None
