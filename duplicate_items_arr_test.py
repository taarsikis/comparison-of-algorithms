"""
Для наступних випадків від 2**7 до 2**15:
    1. випадкові числа
    2. відсортований список
    3. відсортований[::-1]
    4. елементи тільки з {1,2,3}
"""
import random
import time

from Generate_plot import generate_plot
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import main as merge_sort
from shell_sort import shell_sort

sorts = ["insertion_sort", "selection_sort", "merge_sort", "shell_sort"]
duplicated_arr = {}
for el in sorts:
    duplicated_arr[el] = {}

for n in range(7, 16):
    print(n)
    arr_len = "2 ** " + str(n)
    arr = [random.randint(1,3) for _ in range(2 ** n)]
    for el in sorts:
        print(el)
        start_time = time.time()
        counter = eval(f"{el}(arr)[1]")
        needed_time = time.time() - start_time
        if needed_time == 0:
            needed_time = 0.0009
        duplicated_arr[f"{el}"][arr_len] = {}
        duplicated_arr[f"{el}"][arr_len]["time"] = needed_time
        duplicated_arr[f"{el}"][arr_len]["counter"] = counter
#
#
generate_plot("в списку з елементів {1,2,3}", duplicated_arr)
print("________ END ________")

