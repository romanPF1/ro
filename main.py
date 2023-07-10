import json
if __name__ == "__main__" :
  #  # with open("data.json", "r") as file:
  #   #    data = json.load(file)
  #   #    print(data['name'])
  # #  x = {
  # #      "name": "John",
  #  #     "age": 25
  #  # }
  #
  # #  y = json.dumps(x)
  #
  # #  with open("data.json","w") as file:
  #  #     json.dump(x, file)
  #  name = input("Vvedity imia uchnya: ")
  #  age = input("Vvedity vik uchnya")
  #
  #  frame_student = {
  #      "name": name,
  #      "age": age
  #  }
  #
  #  with open("students_data.json", "r") as file:
  #      students = json.load(file)
  #      students.append(frame_student)
  #
  #  with open("students_data.json", "w") as f:
  #      json.dump(students, f)
    with open('products.json', "r") as file:
        products = json.load(file)

    for item in products:
        print(item["id"], item["title"])
