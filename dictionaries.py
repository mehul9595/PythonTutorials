class DictionaryExample:
    phonebooks = {}
    phonebooks["mehul"] = 12345677
    phonebooks["akv"] = 1231235093534523
    phonebooks["vihu"] = "123fsafsdf"

    def printItems(self):
        for x, y in self.phonebooks.items():
            print("dictionary key/values are %s => %d", x,y)

    def addItem(self, key, value):
        self.phonebooks[key] = value
    
    def removeItem(self, key):
        self.phonebooks.pop(key)

    def checkIfKeyInDictionary(self, key):
        if key in self.phonebooks:
            return True
        else:
            return False

obj = DictionaryExample()
obj.addItem("abc", 1111)
obj.addItem(2123, 3333)
obj.printItems()
obj.removeItem(2123)
print("\n")
obj.printItems()
check2123value = obj.checkIfKeyInDictionary(2123)
checkabcvalue = obj.checkIfKeyInDictionary("abc")

print(check2123value)
print(checkabcvalue)