import matplotlib.pyplot as plt

def generate_plot(test_type,res):
    sorts = ["insertion_sort", "selection_sort", "merge_sort", "shell_sort"]
    x = list(res["insertion_sort"].keys())
    y = [[res[sort][length]["counter"] for sort in res.keys()] for length in x]
    print(y)
    plt.xlabel("Довжина списку")
    plt.ylabel("К-сть порівнянь")
    plt.title(f"К-сть порівнянь {test_type}")
    for i in range(len(y[0])):
        plt.plot(x,[pt[i] for pt in y],label = sorts[i])
    plt.legend()
    plt.yscale("log", base = 10)
    plt.savefig(f'К-сть порівнянь в {test_type} 1.png')
