class Category:

  def __init__(self, name):

    self.name = name
    self.ledger= list()
    

  def deposit(self, amount, description= ""):
    to_add= {}
    to_add["amount"] = amount
    to_add["description"] = description
    self.ledger.append(to_add)


  def withdraw (self, amount, description= ""):

    apporved = self.check_funds(amount)

    if apporved == False:  
      to_add= {}
      to_add["amount"] = amount* -1
      to_add["description"] = description
      self.ledger.append(to_add)
      return True

    else:
      return False


  def get_balance(self):
    self.current_balance = 0

    for each in self.ledger:
      dic = each
      self.current_balance += dic["amount"]

    return self.current_balance


  def transfer(self, amount, where_to):
    to_account= where_to.name
    
    self.apporved = self.check_funds(amount)
    
    if self.apporved == False:
      description_to= "Transfer to {}".format(to_account)
      self.withdraw(amount, description_to)
      
      description_from= "Transfer from {}".format(self.name)
      where_to.deposit(amount, description_from)

      return True
    
    else:
      return False


  def check_funds(self, amount):
    
    self.funds = self.get_balance()

    if amount < self.funds:
      return False #Approved
    else:
      return True #NOT Approved

  def __str__(self):
    self.title = self.name.center(30, '*')
    self.one_lista = list()
    self.one_lista.append(self.title)

    for each in self.ledger: #Printing:
      dic = each
  
      descriptions = "{:<23}".format(dic['description'])
      amounts = "{:>7.2f}".format(dic['amount'])

      self.one_lista.append("{:<.23}{:>.7}".format(descriptions, amounts))

    self.total = "Total: "+ str(self.get_balance())

    self.one_lista.append(self.total)
    
    return "\n".join(self.one_lista)

   
#def create_spend_chart(categories):