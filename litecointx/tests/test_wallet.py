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

from bitcointx import ChainParams
from bitcointx.wallet import CCoinAddress, CCoinAddressError

from litecointx import LitecoinMainnetParams
from litecointx.wallet import P2SHLitecoinLegacyAddress


class Test_LitecoinAddress(Test_CCoinAddress):

    def test_address_implementations(self, paramclasses=None):
        super(
            Test_LitecoinAddress, self
        ).test_address_implementations(paramclasses=[LitecoinMainnetParams])

    def test_legacy_p2sh(self):
        with ChainParams('litecoin', allow_legacy_p2sh=True):
            a = CCoinAddress('3F1c6UWAs9RLN2Mbt5bAJue12VhVCorXzs')
            self.assertIsInstance(a, P2SHLitecoinLegacyAddress)

        with ChainParams('litecoin'):
            with self.assertRaises(CCoinAddressError):
                a = CCoinAddress('3F1c6UWAs9RLN2Mbt5bAJue12VhVCorXzs')
