

class Person(object):
    """Do not modify the content of this class"""
    def __init__(self, d: dict):
        """
    Pass dict with person data
        @param d: dict
        """
        self.name = d['name']
        self.name = d['age']


class Client(Person):
    """Do not modify the content of this class"""
    def __init__(self, d: dict):
        """
    Pass dict with client data
        @param d: dict
        """
        super().__init__(d)
        self.id = d['id'] # unique id of the client 
        self.credit_rating = d['credit_rating'] # credit score of the cleint
        self.balance = d['credit_amount'] # the current account availabel money
        self.password = d['secret'] # the password to the client account 


if __name__ == '__main__':
    b = Client
    print(b, id(b))