temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

hot = filter(lambda x: x >= 28, temperatures)
hot_list = list(hot)
print(max(hot_list), min(hot_list), sum(hot_list) / len(hot_list))
