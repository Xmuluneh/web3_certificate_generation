from algosdk.future.transaction import *

txn = PaymentTxn(
    sender=accounts[0].address,
    sp=client.suggested_params(),
    receiver=accounts[1].address,
    amt=1000
)

stxn = txn.sign(accounts[0].private_key)
tx_id = client.send_transaction(stxn)
result =  wait_for_confirmation(client, tx_id, 2)
print(result)