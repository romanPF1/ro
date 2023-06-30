if __name__ == "__main__" :
    someArray = [1, "test", True, 1.6, "hey"]
    # get element by index
    print(someArray[4])
    # lenght array
    print(len(someArray))
    # last element array
    print(someArray[-1])
    # add elements to array
    someArray.append(2)
    print(someArray)
    # Remove element
    someArray.pop(1)
    print(someArray)
    someArray.remove('hey')
    print(someArray)
    # find element in array
    targetElement = someArray.index(1.6)
    print(targetElement)
    # replace
    targetElementIndex = someArray.index(1.6)
    someArray[targetElementIndex] = "test3"
    someArray.reverse()
    print(someArray)
    # clear array
    someArray.clear()
    print(someArray)



    a = [1]
    b = a.copy()
    a[0] += 1
    print(a)
    print(b)

    tempDict = {
        "name": "test"
      }

    print(tempDict['name'])

    temDict = {

    ### personal data
    name = input("Vvedit imia: ")
    surname = input("Vvedit prizvysthe: ")
    fathers_name = input("Vvedit Po-batkovi: ")
    ### format
    name = name.title()
    surname = surname.title()
    fathers_name - fathers_name.title()

    ### create data frame
        "name": surname,
        "surname": surname,
        "fathers_name"{surname}{name}{fathers_name}"
    }
    print(personal_data)




    

    adress = input("Vvedity adres: ")
    misto = input("Vvedity misto: ")
    street = input("Vvedity street: ")
















