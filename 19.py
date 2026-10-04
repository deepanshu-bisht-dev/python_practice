# Income tax with slabs (marginal calculation)
def income_tax(income):
    # (upper limit of slab, rate), hypothetical slabs
    slabs = [(300000, 0.0), (700000, 0.05), (1000000, 0.10),
             (1200000, 0.15), (1500000, 0.20)]
    tax = 0
    prev_limit = 0
    for limit, rate in slabs:
        if income > limit:
            tax += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            tax += (income - prev_limit) * rate
            return tax
    return tax + (income - prev_limit) * 0.30   # above last slab

print(income_tax(900000))   