import json
import os


transactions = []
current_balance = 0

# Ask for file name
file_name = input('Enter a file name to load/save your data: ').strip()
if not file_name.endswith('.json'):
    file_name += '.json'

# Load existing date if file exists
if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
        transactions = data.get('transactions', [])
        current_balance = data.get('balance', 0)
        print('Data loaded')
else:
    print('Starting with a new file.')

# Save function
def save_data():
    with open(file_name, 'w') as f:
        json.dump({'transactions': transactions, 'balance': current_balance}, f)


while True:
    main_menu = input('What do you want to do?\n1. Add income\n2. Add expense\n'
                      '3. Show transactions\n4. Show balance\n5. Delete transactions\n'
                      '6. Save and quit\nChoice: ')

    if main_menu == '1':
        source = input('Where did the income come from?: ')
        amount = input('How much was the income?: ')
        if amount.isdigit():
            transactions.append({
                'type': 'income',
                'source': source,
                'amount': int(amount)
            })
            current_balance += int(amount)
            print('Income added.')
        else:
            print('Amount must be a number.')

    elif main_menu == '2':
        category = input('What was the expanse for?: ')
        expanse_amount = input('How much was the expanse?: ')
        if expanse_amount.isdigit():
            transactions.append({
                'type': 'expanse',
                'category': category,
                'amount': int(expanse_amount)
            })
            current_balance -= int(expanse_amount)
            print('Expanse added.')
        else:
            print('Amount must be a number.')

    elif main_menu == '3':
        for t in transactions:
            if t['type'] == 'income':
                print(f"Income: {t['amount']} from {t['source']}")
            elif t['type'] == 'expanse':
                print(f"Expanse: {t['amount']} for {t['category']}")

    elif main_menu == '4':
        print(f'Your current balance is {current_balance}.')

    elif main_menu == '5':
        if not transactions:
            print('No transactions to delete.')
            continue

        print('Transactions:')
        for idx, t in enumerate(transactions, 1):
            if t['type'] == 'income':
                print(f"{idx}. Income: {t['amount']} from {t['source']}")
            elif t['type'] == 'expanse':
                print(f"{idx}. Expanse: {t['amount']} from {t['category']}")

        delete_idx = input('Enter the number of the transaction to delete: ')
        if delete_idx.isdigit():
            delete_idx = int(delete_idx)
            if 1 <= delete_idx <= len(transactions):
                deleted = transactions.pop(delete_idx - 1)

                # Adjust balance based on the deleted transactions
                if deleted['type'] == 'income':
                    current_balance -= deleted['amount']
                elif deleted['type'] == 'expanse':
                    current_balance += deleted['amount']

            else:
                print('Invalid number.')
        else:
            print('Please enter a valid number.')

    elif main_menu == '6':
        save_data()
        print('Data saved. Goodbye!')
        break

    else:
        print('Invalid choice. Try again.')