income = 250_000

lowtaxland_rate = 0.05
ripoffland_rate = 0.43
lowlandlandTaxAmout = income*lowtaxland_rate
ripofflandTaxAmout = income*ripoffland_rate


print('Your income is',income,'and you would pay',lowlandlandTaxAmout,'income tax in Lowtaxland or',ripofflandTaxAmout,'income tax in Ripoffland. You would save',ripofflandTaxAmout - lowlandlandTaxAmout ,'by paying taxes in Lowtaxland!')