import json
if __name__ == "__main__" :
    with open("products.json", "r", encoding="utf-8") as file:
      #   products = json.load(file)
      #  total_price = 0
      #  for item in products:

       #     price = item['price'].replace("NBSP", "").replace(" ", "")
       #     item[price] = price
       #     total_price += int(price)
      #  print(total_price)
      #  new_list_products = []
       # for item in products:
           # print(item['colors'])
        #    for color in (item['colors']):
         #       print(color)
          #      if color.lower() == "чорний":
           #         print(item)
            #        new_list_products.append(item)
      #  print(new_list_products)

      #  new_list_products = []
       # for item in products:
        #    if "Чорний" in item['colors']:
         #       new_list_products.append(item)


      #  print(new_list_products)

      #  some_arr = [1, 2, 2, 3]
      #  unique_val = []

      #  for el in some_arr:
       #     if el in unique_val:
       #         continue
      #      else:
      #          unique_val.append(el)

      #  print(unique_val)

         products = json.load(file)
         new_list_product = []

        # for value in (item['value']):
        #     for item in products:
        #         print(value)
        #     print(item['value'])
        #     if value.lower() == "А ++":
        #         print(item)

         # for item in products:
         #     # print(item['features'])
          #     for el in item['features']:
          #         if el['value'] == "А++":
          #             print(el)
        # for item in products:
        #     for feature in item['features']:
        #         if feature['value'] == "А++":
        #             print(item["title"], feature)


    print(products)

    prices = []

    for item in products:
        product_price = int(item['price'].replace(" ", "").replace(" ", ""))
        prices.append(product_price)

    print(prices)

    abs_prices = sorted(prices)
    print(abs_prices)
    desc_price = sorted(prices, reverse=True)
    print(desc_price)
    for i in range(5):
        print(desc_price[i])
