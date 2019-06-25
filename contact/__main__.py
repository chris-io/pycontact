import intern

import time



while True:
    print("available tasks are: [add], [read], [update], [del], [exit] ")
    operation = input("task ~$")
    if operation == "exit":
        for i in range(10):
            print(".")
            time.sleep(0.02)
        break

    if operation == "read":
        obj = intern.contact()
        select = input("select by 'name' or 'fav' or 'all'--> ")

        if select.lower() == "name":
            name = input(select.lower() + " -->")
            if len(name) > 0:
                info = obj.read(name=name)
                for kw in info:
                    print("{} : {}".format(kw,info[kw]),end="\n")
        if select.lower() == "all":
            info = obj.read(all=True)
            print("=" * 40)
            for contact in info:
                for kw in contact:
                    print("{} : {}".format(kw,contact[kw]),end="\n")
                print("=" * 40)

    if operation == "del" :
        obj = intern.contact()
        select = input("name --> ").lower()
        if obj.delc(name=select) == True:
            print("{} deleted successfully ".format(select))
    if operation == "add" :
        name = input("name --> ")
        if name == "exit":
            for i in range(10):
                print(".")
                time.sleep(0.02)
            break
        if len(name) >= 1 :
            tel = input("phone number --> ")
            if tel == "exit":
                for i in range(10):
                    print(".", end='')
                    time.sleep(0.02)
                break
            if len(tel) == 9 :
                fav = input("fav ? ['yes' or 'no']")
                if fav == "exit":
                    for i in range(10):
                        print(".")
                        time.sleep(0.02)
                    break
                if fav ==  "yes" or fav ==  "no":
                    if fav == "yes":  fav = True
                    elif fav == "no": fav = False

                    obj = intern.contact()
                    if obj.addc(name=name,tel=tel,fav=fav) == True:
                        print(name + " was added ")
    if operation == "update":
        obj = intern.contact()
        name = input("name --> ")
        if obj.exist(name):
            tel = input("new tel --> ")
            if obj.updatec(name=name, tel=tel) == True:
                print("{} was updated successfully".format(name))
            else:
                print("something went wrong")
        else:
            print("error occured", end="\n")
