#  I got curious about what my federal tax burden would be this year, but never really found a program written to handle it.
#  So I wrote one! Based on the information found here: http://onforb.es/1JaKokB
#  If you insert your 2015 taxable income into the 'calctax' function, you'll get a full print out of your 2015 tax burden and
#  your effective tax rate.
#  Enjoy!...er, maybe my next program will be a digital Kleenex box to wipe your tears with...

def calctax(taxableincome):
    tb1 = 1845
    tb2 = 10313
    tb3 = 29388
    tb4 = 51578
    tb5 = 111324
    tb6 = 129997
    tb7 = 464850
    
    if taxableincome < 18450:
        tb1 = int(taxableincome * .1)
        print "In tax bracket 1 (10%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(taxableincome, tb1)
        print "Your effective tax rate is 10 percent of your hard-earned money!"
    elif taxableincome > 18450 and taxableincome <= 74900:
        tax = int((taxableincome - 18450) * .15)
        print "In tax bracket 1 (10%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(18450, tb1)
        print "In tax bracket 2 (15%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format((taxableincome - 18450), tax)
        print "The total tax burden for your ${:,} taxable income would be ${:,}.".format(taxableincome, tb1 + tax)
        print "Your effective tax rate is %.2f percent of your hard-earned money!" % (float(tb1 + tax) / float(taxableincome))
    elif taxableincome > 74900 and taxableincome <= 151200:
        tax = int((taxableincome - 74900) * .25)
        print "In tax bracket 1 (10%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(18450, tb1)
        print "In tax bracket 2 (15%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(74900, tb2)
        print "In tax bracket 3 (25%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format((taxableincome - 74900), tax)
        print "The total tax burden for your ${:,} taxable income would be ${:,}.".format(taxableincome, tb2 + tax)
        print "Your effective tax rate is %.2f percent of your hard-earned money!" % (float(tb2 + tax) / float(taxableincome))
    elif taxableincome > 151200 and taxableincome <= 230450:
        tax = int((taxableincome - 151200) * .28)
        print "In tax bracket 1 (10%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(18450, tb1)
        print "In tax bracket 2 (15%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(74900, tb2)
        print "In tax bracket 3 (25%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(151200, tb3)
        print "In tax bracket 4 (28%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format((taxableincome - 151200), tax)
        print "The total tax burden for your ${:,} taxable income would be ${:,}.".format(taxableincome, tb3 + tax)
        print "Your effective tax rate is %.2f percent of your hard-earned money!" % (float(tb3 + tax) / float(taxableincome))
    elif taxableincome > 230451 and taxableincome <= 411500:
        tax = int((taxableincome - 230451) * .33)
        print "In tax bracket 1 (10%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(18450, tb1)
        print "In tax bracket 2 (15%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(74900, tb2)
        print "In tax bracket 3 (25%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(151200, tb3)
        print "In tax bracket 4 (28%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(230451, tb4)
        print "In tax bracket 5 (33%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format((taxableincome - 230451), tax)
        print "The total tax burden for your ${:,} taxable income would be ${:,}.".format(taxableincome, tb4 + tax)
        print "Your effective tax rate is %.2f percent of your hard-earned money!" % (float(tb4 + tax) / float(taxableincome))
    elif taxableincome > 411500 and taxableincome <= 464850:
        tax = int((taxableincome - 411500) * .35)
        print "In tax bracket 1 (10%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(18450, tb1)
        print "In tax bracket 2 (15%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(74900, tb2)
        print "In tax bracket 3 (25%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(151200, tb3)
        print "In tax bracket 4 (28%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(230450, tb4)
        print "In tax bracket 5 (33%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(411500, tb5)
        print "In tax bracket 6 (35%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format((taxableincome - 411500), tax)
        print "The total tax burden for your ${:,} taxable income would be ${:,}.".format(taxableincome, tb5 + tb6)
        print "Your effective tax rate is %.2f percent of your hard-earned money!" % (float(tb5 + tax) / float(taxableincome))
    elif taxableincome > 464850:
        tax = int((taxableincome - 464850) * .396)
        print "In tax bracket 1 (10%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(18450, tb1)
        print "In tax bracket 2 (15%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(74900, tb2)
        print "In tax bracket 3 (25%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(151200, tb3)
        print "In tax bracket 4 (28%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(230450, tb4)
        print "In tax bracket 5 (33%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(411500, tb5)
        print "In tax bracket 6 (35%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format(464850, tb6)
        print "In tax bracket 7 (39.6%): Your taxable income was ${:,}, and your tax burden is ${:,}.".format((taxableincome - 411500), tax)
        print "The total tax burden for your ${:,} taxable income would be ${:,}.".format(taxableincome, tb6 + tax)
        print "Your effective tax rate is %.2f percent of your hard-earned money!" % (float(tb6 + tax) / float(taxableincome))
    else:
        print "You messed up somewhere!"
