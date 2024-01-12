from algosdk import account, template
from algosdk.future.transaction import suggested_params, compileTeal
from algosdk.logic import logic_signature
from util import (
    create_payment_transaction,
    process_logic_sig_transaction,
    process_transactions,
    account_balance,
    transaction_info,
    add_standalone_account,
    fund_account,
)
from pyteal import And, Global, Int, Mode, Txn, TxnType

BANK_ACCOUNT_FEE = 1000


def bank_for_account(receiver):
    """Create a condition allowing the receiver to withdraw funds from the contract account."""
    return And(
        Txn.type_enum() == TxnType.Payment,
        Global.group_size() == Int(1),
        Txn.receiver() == Addr(receiver),
        Txn.close_remainder_to() == Global.zero_address(),
        Txn.rekey_to() == Global.zero_address(),
        Txn.fee() <= Int(BANK_ACCOUNT_FEE),
    )


def create_bank_transaction(logic_sig, escrow_address, receiver, amount, fee=1000):
    """Create a bank transaction with the provided amount."""
    params = suggested_params()
    params.fee = fee
    params.flat_fee = True
    payment_transaction = create_payment_transaction(escrow_address, params, receiver, amount)
    transaction_id = process_logic_sig_transaction(logic_sig, payment_transaction)
    return transaction_id


def setup_bank_contract(**kwargs):
    """Initialize and return a bank contract for the provided receiver."""
    receiver = kwargs.pop("receiver", add_standalone_account()[1])
    teal_source = compileTeal(bank_for_account(receiver), mode=Mode.Signature, version=3)
    logic_sig = logic_signature(teal_source)
    escrow_address = logic_sig.address()
    fund_account(escrow_address)
    return logic_sig, escrow_address, receiver


def _create_grouped_transactions(split_contract, amount):
    """Create grouped transactions for the provided split contract and amount."""
    params = suggested_params()
    return split_contract.get_split_funds_transaction(
        split_contract.get_program(), amount, 1, params.first, params.last, params.gh
    )


def _create_split_contract(
    owner, receiver_1, receiver_2, rat_1=1, rat_2=3, expiry_round=5000000, min_pay=3000, max_fee=2000
):
    """Create and return a split template instance from the provided arguments."""
    return template.Split(owner, receiver_1, receiver_2, rat_1, rat_2, expiry_round, min_pay, max_fee)


def create_split_transaction(split_contract, amount):
    """Create a transaction with the provided amount for the provided split contract."""
    transactions = _create_grouped_transactions(split_contract, amount)
    transaction_id = process_transactions(transactions)
    return transaction_id


def setup_split_contract(**kwargs):
    """Initialize and return a split contract instance based on the provided named arguments."""
    owner = kwargs.pop("owner", add_standalone_account()[1])
    receiver_1 = kwargs.pop("receiver_1", add_standalone_account()[1])
    receiver_2 = kwargs.pop("receiver_2", add_standalone_account()[1])

    split_contract = _create_split_contract(owner, receiver_1, receiver_2, **kwargs)
    escrow_address = split_contract.get_address()
    fund_account(escrow_address)
    return split_contract


if __name__ == "__main__":
    _, local_receiver = add_standalone_account()
    amount = 5000000
    logic_sig, escrow_address, receiver = setup_bank_contract(receiver=local_receiver)
    assert receiver == local_receiver

    transaction_id = create_bank_transaction(logic_sig, escrow_address, local_receiver, amount)
    print(f"amount: {amount}")
    print(f"escrow: {escrow_address}")
    print(f"balance_escrow: {account_balance(escrow_address)}")
    print(f"balance_receiver: {account_balance(local_receiver)}")
    print(json.dumps(transaction_info(transaction_id), indent=2))

    print("\n\n")

    _, local_owner = add_standalone_account()
    _, local_receiver_2 = add_standalone_account()
    amount = 5000000

    split_contract = setup_split_contract(owner=local_owner, receiver_2=local_receiver_2, rat_1=3, rat_2=7)
    assert split_contract.owner == local_owner
    assert split_contract.receiver_2 == local_receiver_2

    transaction_id = create_split_transaction(split_contract, amount)

    print(f"amount: {amount}")
    print(f"escrow: {split_contract.get_address()}")
    print(f"balance_escrow: {account_balance(split_contract.get_address())}")
    print(f"owner: {split_contract.owner}")
    print(f"balance_owner: {account_balance(split_contract.owner)}")
    print(f"receiver_1: {split_contract.receiver_1}")
    print(f"balance_1: {account_balance(split_contract.owner)}")
