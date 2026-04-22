def flat(nested_arr):
    flat_new= []

    for el in nested_arr:
        for x in el:
            flat_new.append(x)

    print(flat_new)

flat([[1,2,3],[4,5],[6]])

