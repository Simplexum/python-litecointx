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

from .version import __version__

import litecointx.core
import litecointx.wallet

from bitcointx import BitcoinMainnetParams


# Declare chain params after frontend classes are regstered in wallet.py,
# so that issubclass checks in ChainParamsMeta.__new__() would pass
class LitecoinMainnetParams(BitcoinMainnetParams):
    NAME = 'litecoin'
    RPC_PORT = 9332
    TRANSACTION_IDENTITY = litecointx.core.LitecoinTransactionIdentityMeta
    WALLET_IDENTITY = litecointx.wallet.LitecoinWalletIdentityMeta


class LitecoinTestnetParams(LitecoinMainnetParams):
    NAME = 'litecoin/testnet'
    RPC_PORT = 19332
    WALLET_IDENTITY = litecointx.wallet.LitecoinTestnetWalletIdentityMeta


class LitecoinRegtestParams(LitecoinMainnetParams):
    NAME = 'litecoin/regtest'
    RPC_PORT = 19443
    WALLET_IDENTITY = litecointx.wallet.LitecoinRegtestWalletIdentityMeta


__all__ = (
    '__version__',
    'LitecoinMainnetParams',
    'LitecoinTestnetParams',
    'LitecoinRegtestParams'
)
