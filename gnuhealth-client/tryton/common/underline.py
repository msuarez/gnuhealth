# This file is part of GNU Health.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.


def set_underline(label):
    "Set underscore for mnemonic accelerator"
    return '_' + label.replace('_', '__')
