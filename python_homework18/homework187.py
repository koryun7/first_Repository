def swap_tuples(tuple1, tuple2):
    return tuple2, tuple1

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')


print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

tuple1, tuple2 = swap_tuples(tuple1, tuple2)

print("\n")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)