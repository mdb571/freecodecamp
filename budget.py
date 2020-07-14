class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]

    def deposit(self,amount,description=''):
        self.ledger.append({"amount":amount,"description":description})

    def withdraw(self,amount,desciption=''):
        if self.check_funds(amount):
            self.ledger.append({"amount":(0-amount),"description":desciption})
            return True
        else:
            return False

    def get_balance(self):
        total=0
        for elem in self.ledger:
            total+=elem['amount']
        return total
    
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,"Transfer to "+category.name)
            category.deposit(amount,"Transfer from "+self.name)
            return True
        else:return False


    def check_funds(self,amount):
        if self.get_balance()<amount:
            return False
        else:
            return True

    def __str__(self):
        out=self.name.center(30,"*")
        for elem in self.ledger:
            out+='\n'+elem['description'][:23].ljust(23)+str("%.2f"%float(elem['amount'])).rjust(7)
        out+='\n'+"Total: "+str("%.2f"%float(self.get_balance()))
        return out

def totaldep(category):
    return sum([-i["amount"] for i in category.ledger if i["amount"] < 0])



def create_spend_chart(categories):
    graph = "Percentage spent by category\n"
    total = 0
    percentage = {}

    for category in categories:
        percentage[category.name] = totaldep(category)
        total += totaldep(category)

    for key in percentage:
        percentage[key] *= (100/total)
        percentage[key] = int(percentage[key])

    for i in range(100, -1, -10):
        graph += (str(i) + "| ").rjust(5, " ")
        for key in percentage:
            if percentage[key] >= i:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"
    graph += "    ----" + "---"*(len(categories)-1) + "\n     "
    
    length = 0
    names = []
    for category in categories:
        name = category.name
        names.append(name)
        if len(name) > length:
            length = len(name)

    for i in range(length):
        for name in names:
            if len(name) > i:
                graph += name[i] + "  "
            else:
                graph += "   "

        if i < length-1:
            graph += "\n     "
    return graph