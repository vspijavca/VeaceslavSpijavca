
class Bank(object):
    """ Class responsible for:
        - managing the clients objects and transaction methods
        - changing clients real time data
        - checking transaction validity criteria
        You can add other methods to this class to suite your needs and logic
        You must write the logic for the already defined methods and their goals (renaming them and the invocation type is prohibited as I will use them only when evaluating your code)
    """

    def __init__(self, json_path: str):
        """
    Here you need to:
    - Pass as argument the correct json path > Store the json file path in the object, handle situation when the path is invalid
    - read data from the json file and instantiate the client objects in a collection
    - It is up to you to decide how to store and handle further the bank clients data
    Each client has a unique id value therefore in your operations you should use it as unique identifier
    In this constructor you can define whatever object variables you consider necessary.
        """
        pass

    def get_client(self, id: str):
        """Will return the respective client object that has the inputted unique id"""
        
        pass

    def withdraw_amount(self, client_id, amount, secret = None) -> bool:
        """
    Substract form a client account the passed amount. Conditions for the substaraction to be allowed:
    1. the result of substaraction must not make the balance negative
    2. the secret variabel must be identical with the client password
    In case all the of the above conditions are meet modify the client accout balance accordingly and return True, otherwise do not modify client balance and return False
        """
        pass

    def supply_amount(self, client_id: str, amount: int) -> bool:
        """
    Add up to the client acocunt balance. The amount that you pass to this method must follow the following rules in order to be considered valid:
    1 it must be a positive, integer number
    2 it must not exeed the product of the account balance multiplied by the credit rating figure
        """
        pass


if __name__ == '__main__':
    x = Bank('some_json_file_location')
    print(x)
