# Copyright (C) 2019 The python-litecointx developers
#
# This file is part of python-litecointx.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-litecointx, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

# pylama:ignore=E501

from bitcointx.tests.test_wallet import Test_CCoinAddress

from litecointx import LitecoinMainnetParams


class Test_LitecoinAddress(Test_CCoinAddress):

    def test_address_implementations(self, paramclasses=None):
        super(
            Test_LitecoinAddress, self
        ).test_address_implementations(paramclasses=[LitecoinMainnetParams])
