import timeit
from functools import partial
import sys
sys.path.append("..")

import task_0.yaml_to_xml
import dop_1.yaml_to_xml
import dop_2.yaml_to_xml
import dop_3.yaml_to_xml

# Определяем функции для вызова с помощью partial
task_00 = task_0.yaml_to_xml.process
dop11 = dop_1.yaml_to_xml.process
dop22 = dop_2.yaml_to_xml.process
dop33 = dop_3.yaml_to_xml.convert_yaml_to_xml
# Используем timeit для каждой функции, исполняя её 100 раз
t1 = ("task_0", timeit.timeit(task_00, number=100))
t3 = ("dop_1", timeit.timeit(dop11, number=100))
t2 = ("dop_2", timeit.timeit(dop22, number=100))
t4 = ("dop_3", timeit.timeit(dop33, number=100))

# Сортировка и вывод времени
all_times = [t1, t2, t3, t4]
sorted_times = sorted(all_times, key=lambda x: x[1])
print(all_times)
