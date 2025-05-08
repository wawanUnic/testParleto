from django.db import transaction
import csv

from django.core.exceptions import ValidationError

from statements.models import Account, Statement, StatementItem

def statement_import(file_handler):
    idx = 0
    statement_buffer = []
    # _T_O_D_O_: TASK → in case of errors database must not change ------
    # _T_O_D_O_: TASK → optimize database queries during import ------
    try:
        with transaction.atomic():
            for row in csv.DictReader(file_handler):
                account, _ = Account.objects.get_or_create(
                    name=row['account'],
                    defaults={'currency': row['currency']}
                )[0]
                if account.currency != row['currency']:
                    raise ValidationError('Invalid currency currency ')

                statement, _ = Statement.objects.get_or_create(
                    account=account,
                    date=row['date']
                )[0]

                statement_buffer.append(
                    StatementItem(
                        statement=statement,
                        amount=row['amount'],
                        currency=row['currency'],
                    )
                )

#                StatementItem.objects.create(
#                    statement=statement,
#                    amount=row['amount'],
#                    currency=row['currency'],
#                )

                idx += 1

            StatementItem.objects.bulk_create(statement_buffer)

    except Exception as e:
        print(f"Error: {e}")
        return 0
    return idx

