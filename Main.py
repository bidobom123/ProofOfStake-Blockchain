from Transaction import Transaction
if __name__ == '__main__':

    sender = 'sender'
    receiver= 'receiver'
    amount = 1
    type = 'TRANSFER'
    transaction = Transaction(sender, receiver,amount,type)
    print(transaction.tojson())

