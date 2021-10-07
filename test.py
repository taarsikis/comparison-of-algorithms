import matplotlib.pyplot as plt
sorts = ["insertion_sort", "selection_sort", "merge_sort", "shell_sort"]
res = {'insertion_sort': {'2 ** 7': {'time': 0.0019974708557128906, 'counter': 3940}, '2 ** 8': {'time': 0.009994745254516602, 'counter': 15347}, '2 ** 9': {'time': 0.04597330093383789, 'counter': 68843}}, 'selection_sort': {'2 ** 7': {'time': 0.00299835205078125, 'counter': 8128}, '2 ** 8': {'time': 0.005996227264404297, 'counter': 32640}, '2 ** 9': {'time': 0.03897881507873535, 'counter': 130816}}, 'merge_sort': {'2 ** 7': {'time': 0.0010027885437011719, 'counter': 864}, '2 ** 8': {'time': 0.0019991397857666016, 'counter': 2851}, '2 ** 9': {'time': 0.005996227264404297, 'counter': 7325}}, 'shell_sort': {'2 ** 7': {'time': 0.0009963512420654297, 'counter': 1658}, '2 ** 8': {'time': 0.00299835205078125, 'counter': 4161}, '2 ** 9': {'time': 0.008994579315185547, 'counter': 12185}}}

x = list(res["insertion_sort"].keys())
y = [[res[sort][length]["time"] for sort in res.keys()] for length in x]
plt.xlabel("Довжина списку")
plt.ylabel("Час роботи")
plt.title("Час роботи сортувань в ...")
for i in range(len(y[0])):
    plt.plot(x,[pt[i] for pt in y],label = sorts[i])
plt.legend()
plt.show()