import json
if __name__ == "__main__" :


    #
    # for i in range(1, 3):
    #     print(i)
    #     print(arr[i])
    # numbers = []
    # for i in range(1, 101, 1):
    #     numbers.append(i)
    # print(numbers)
    # even_numbers = []
    # odd_numbers = []
    # for i in numbers:
    #     if i % 2 == 0:
    #         even_numbers.append(i)
    #     else:
    #         odd_numbers.append(i)
    #     print(even_numbers)
    #     print(odd_numbers)

    #sort

    # arr = [4, 56, 2, 6, 3, 89]
    # flag = Truewhile
    # flag:
    # flag = False
    # status_check = True
    # for i in range(len(arr) - 1):
    #     if arr[i] > arr[i + 1]:
    #         print(arr[i], " ", arr[i + 1])
    #         temp = arr[i]
    #         arr[i] = arr[i + 1]
    #         arr[i + 1] = temp
    #
    # print(arr)
    # for item in range(len(arr) - 1):
    #     print(arr[item], " CHECK  ", arr[item + 1])
    #     if arr[item] > arr[item + 1] and flag == False:
    #         flag = Trueprint(arr)

        # arr_two.sort()
        # # print(arr_two)
        # # arr_two.sort()
        # # DESC
        # new_val_desc = sorted(arr_two, revevers=True)

       # str_arr = ["John", "Ann", "Ketty", "Zak"]
        # ___A-Z___
       # sort_az_arr = sorted(str_arr)
        #print(sort_az_arr)
      #  sort_za_arr = sorted(str_arr)
      #  print(sort_za_arr)

    with open('products.json', 'r', encoding="utf-8") as file:
        products = json.load(file)

    #     data = json.load(file)
    # data_sort = []
    # for item in data:
    #     data_sort.append(item['title'])
    # data_sort = sorted(data_sort)
    # print(data_sort)
    products.sort(key=lambda x: x ["price"])
    sorted_product = sorted(products, key=lambda product: product["price"], reverese=True)
    print(sorted_product)

    with open("products_as.json", "w", encoding="utf-8") as file:
        json.dump(products, file)




















