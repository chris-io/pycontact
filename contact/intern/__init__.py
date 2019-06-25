
class contact():
    #contact: {"contact":{id1:{"name":{"firstname":"Alex","lastename":"Takam"},"tel":["696747714","694784353"]},id2: ...},"count":0}
    #this is my primary model
    import shelve, random, getpass, os
    def __init__(self):
        if self.os.path.isdir("C:/users/" + self.getpass.getuser() + "/documents/iobank"):
            self.bank = self.shelve.open("C:/users/" + self.getpass.getuser() +"/documents/iobank/bank",writeback=True)
        else:
            self.os.mkdir("C:/users/" + self.getpass.getuser() +"/Documents/iobank")
            self.bank = self.shelve.open("C:/users/" + self.getpass.getuser() +"/documents/iobank/bank",writeback=True)

    def addc(self, **kwargs):    #takes args firstname,lastname,tel,fav
        #let's check if we have what is required
        if  ("name" in kwargs)  and ("tel" in kwargs) and ("fav" in kwargs):
            info = {
                self.bicode("name") : self.bicode(kwargs["name"]),
                self.bicode("tel") :  self.bicode(kwargs["tel"]),
                self.bicode("fav") : kwargs["fav"]
            }
            self.bank[self.bicode(kwargs["name"])] = info

            self.bank.sync()

        return True
    def delc(self, **kwargs):       #takes args id
        status = None
        if "name" in kwargs:
            if self.bicode(kwargs["name"]) in self.bank.keys():
                del self.bank[self.bicode(kwargs["name"])]
                status = True
        else:
            status = False
        return status


    def updatec(self, **kwargs):
        status = None
        if "name" in kwargs:
            if self.bicode(kwargs["name"]) in self.bank.keys():
                if "tel" in kwargs:
                    self.bank[self.bicode(kwargs["name"])][self.bicode("tel")] = self.bicode(kwargs["tel"])
                    self.bank.sync()

                    status = True
                else:
                    status = False
            else:
                status = False
        else:
            status = False
        return status

    def bicode(self, plain):
        #step 1: split the entry into arrays   as [arr]
        #step 2: create an ascii equivalence of [arr]
        #step 3: from the ascii eauivalent, create a 2dimentional array
        arr = list(plain)
        bicoded = [[],[]]
        bicodedc = [[],[]]      #it's a 2dimentional array, keep this in mind
        bicode = ""
        # bicoded: [a,b]  where a = int(ascrr[x] / 2) and b = ascrr[x] % 2
        for i in range(len(arr)):
            bicoded[0].append(int(ord(arr[i]) / 2))
            bicoded[1].append(ord(arr[i]) % 2)
            bicodedc[0].append(chr(bicoded[0][i]))
            bicodedc[1].append(chr(bicoded[1][i]))

        bicode = ''.join(bicodedc[0]) + "," + ''.join(bicodedc[1])
        return bicode

    def dicode(self,bicode):
        bicodedc = [[],[]]
        bicharr = bicode.split(',')
        bicodedc[0] = list(bicharr[0])
        bicodedc[1] = list(bicharr[1])
        bicoded = [[],[]]
        ascrr= []
        chrr = []
        for i in range(len(bicodedc[0])):
            bicoded[0].append(ord(bicodedc[0][i]))
            bicoded[1].append(ord(bicodedc[1][i]))

            ascrr.append(bicoded[0][i] * 2 + bicoded[1][i])

            chrr.append(chr(ascrr[i]))

        return ''.join(chrr)
    def read(self,**kwargs):

        if "name" in kwargs:
            result = {}
            for contact in self.bank:
                bicontact = self.dicode(contact)
                if bicontact == kwargs["name"]:
                    print("({}, {})".format(bicontact, kwargs["name"]))

                    result = {
                        "name" : self.dicode(self.bank[contact][self.bicode("name")]),
                        "tel" : self.dicode(self.bank[contact][self.bicode("tel")]),
                        "fav" : self.bank[contact][self.bicode("fav")]
                    }
        if "all" in kwargs:
            result = list()
            if kwargs["all"] == True:
                for contact in self.bank:
                    bicontact = self.dicode(contact)

                    dicter = {
                            "name" : self.dicode(self.bank[contact][self.bicode("name")]),
                            "tel" : self.dicode(self.bank[contact][self.bicode("tel")]),
                            "fav" : self.bank[contact][self.bicode("fav")]
                    }
                    result.append(dicter)

        return result
    def exist(self, name):
        status = None
        if self.bicode(name) in self.bank.keys():
            status = True
        else:
            status = False
        return status
    def closeBank(self):
        self.bank.close()
