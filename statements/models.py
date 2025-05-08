from django.db import models
from django.db.models import Sum

from datetime import datetime

def report_turnover_by_year_month(period_begin, period_end):
    # _T_O_D_O_: TASK → make report using 1 database query without any math in python ---------
    start_date = datetime.strptime(period_begin, "%Y-%m-%d")
    end_date = datetime.strptime(period_end, "%Y-%m-%d")
    turnover_report = StatementItem.objects.filter(
        statement__date__range=(start_date, end_date)
    ).values(
        "statement__date__year", "statement__date__month", "currency"
    ).annotate(
        total_amount=Sum("amount")
    )

    formatted_report = {}
    for item in turnover_report:
        year_month = f"{item['statement__date__year']}-{item['statement__date__month']:02d}"
        if year_month not in formatted_report:
            formatted_report[year_month] = {"incomes": {}, "expenses": {}}

        if item["total_amount"] > 0:
            formatted_report[year_month]["incomes"][item["currency"]] = item["total_amount"]
        else:
            formatted_report[year_month]["expenses"][item["currency"]] = abs(item["total_amount"])

    return formatted_report


class Account(models.Model):
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def for_balance(self):
        total = StatementItem.objects.filter(statement__account=self).aggregate(models.Sum('amount'))['amount__sum']
        self.balance = total if total is not None else 0.00
        self.save()
    # _T_O_D_O_: TASK → add field balance that will update automatically  --------
     
    def __str__(self):
        return f'{self.name}[{self.currency}- {self.balance}]'


class Statement(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    date = models.DateField()
    # _T_O_D_O_: TASK → make sure that account and date is unique on database level --------

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['account', 'date'], name='unique_account_date')
        ]

    def __str__(self):
        return f'{self.account} → {self.date}'
    

class StatementItem(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=3)
    title = models.CharField(max_length=100)
    comments = models.TextField(blank=True, null=True)
    # _T_O_D_O_:  TASK → add field comments (type text) ---------
    

    def __str__(self):
        return f'[{self.statement}] {self.amount} {self.currency} → {self.title} ({self.comments})'
