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
import litecointx.core.script
import litecointx.wallet

from bitcointx import ChainParamsBase


# Declare chain params after frontend classes are regstered in wallet.py,
# so that issubclass checks in ChainParamsMeta.__new__() would pass
class LitecoinMainnetParams(ChainParamsBase,
                            name=('litecoin', 'litecoin/mainnet')):
    RPC_PORT = 9332
    WALLET_DISPATCHER = litecointx.wallet.WalletLitecoinClassDispatcher

    def __init__(self, allow_legacy_p2sh: bool = False) -> None:
        super().__init__()
        self.allow_legacy_p2sh = allow_legacy_p2sh


class LitecoinTestnetParams(LitecoinMainnetParams, name='litecoin/testnet'):
    RPC_PORT = 19332
    WALLET_DISPATCHER = litecointx.wallet.WalletLitecoinTestnetClassDispatcher

    def get_datadir_extra_name(self) -> str:
        return 'testnet4'

    def get_network_id(self) -> str:
        return "test"


class LitecoinRegtestParams(LitecoinMainnetParams, name='litecoin/regtest'):
    RPC_PORT = 19443
    WALLET_DISPATCHER = litecointx.wallet.WalletLitecoinRegtestClassDispatcher


__all__ = (
    '__version__',
    'LitecoinMainnetParams',
    'LitecoinTestnetParams',
    'LitecoinRegtestParams'
)
