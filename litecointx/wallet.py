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

from bitcointx.wallet import (
    CoinWalletIdentityMeta,
    CCoinAddress, P2SHCoinAddress, P2WSHCoinAddress,
    P2PKHCoinAddress, P2WPKHCoinAddress,
    CBase58CoinAddress, CBech32CoinAddress,
    CBase58CoinAddressCommon, CBech32CoinAddressCommon,
    CCoinAddressBase, P2SHCoinAddressCommon, P2PKHCoinAddressCommon,
    P2WSHCoinAddressCommon, P2WPKHCoinAddressCommon,
    CBase58CoinKeyBase, CBase58CoinExtKeyBase, CBase58CoinExtPubKeyBase,
    CCoinKey, CCoinExtKey, CCoinExtPubKey
)

import litecointx
from bitcointx import GetCurrentChainParams
from bitcointx.core.script import CScript
from .core.script import CLitecoinScript


class LitecoinWalletIdentityMeta(CoinWalletIdentityMeta):
    @classmethod
    def _get_extra_classmap(cls):
        return {CScript: CLitecoinScript}


class LitecoinTestnetWalletIdentityMeta(LitecoinWalletIdentityMeta):
    ...


class LitecoinRegtestWalletIdentityMeta(LitecoinWalletIdentityMeta):
    ...


class CLitecoinAddress(CCoinAddressBase,
                       metaclass=LitecoinWalletIdentityMeta):
    ...


class CLitecoinTestnetAddress(CCoinAddressBase,
                              metaclass=LitecoinTestnetWalletIdentityMeta):
    ...


class CLitecoinRegtestAddress(CCoinAddressBase,
                              metaclass=LitecoinRegtestWalletIdentityMeta):
    ...


class CBase58LitecoinAddress(CBase58CoinAddressCommon, CLitecoinAddress):

    @classmethod
    def _get_base58_address_classes(cls):
        params = GetCurrentChainParams()
        if not isinstance(params, litecointx.LitecoinMainnetParams) or\
                not params.allow_legacy_p2sh:
            return (P2SHLitecoinAddress, P2PKHLitecoinAddress)

        # If LitecoinMainnetParams params is not in effect,
        # P2SHLitecoinLegacyAddress can always be instantiated directly.
        # If LitecoinMainnetParams is in effect, and allow_legacy_p2sh
        # is enabled, it will be considered when converting addrs from str.

        return (P2SHLitecoinAddress, P2SHLitecoinLegacyAddress,
                P2PKHLitecoinAddress)


class CBase58LitecoinTestnetAddress(CBase58CoinAddressCommon,
                                    CLitecoinTestnetAddress):
    ...


class CBase58LitecoinRegtestAddress(CBase58CoinAddressCommon,
                                    CLitecoinRegtestAddress):
    ...


class CBech32LitecoinAddress(CBech32CoinAddressCommon, CLitecoinAddress):
    bech32_hrp = 'ltc'


class CBech32LitecoinTestnetAddress(CBech32CoinAddressCommon,
                                    CLitecoinTestnetAddress):
    bech32_hrp = 'tltc'


class CBech32LitecoinRegtestAddress(CBech32CoinAddressCommon,
                                    CLitecoinRegtestAddress):
    bech32_hrp = 'rltc'


class P2SHLitecoinAddress(P2SHCoinAddressCommon, CBase58LitecoinAddress):
    base58_prefix = bytes([50])


class P2SHLitecoinLegacyAddress(P2SHCoinAddressCommon, CBase58LitecoinAddress):
    base58_prefix = bytes([5])


class P2PKHLitecoinAddress(P2PKHCoinAddressCommon, CBase58LitecoinAddress):
    base58_prefix = bytes([48])


class P2WSHLitecoinAddress(P2WSHCoinAddressCommon, CBech32LitecoinAddress):
    ...


class P2WPKHLitecoinAddress(P2WPKHCoinAddressCommon, CBech32LitecoinAddress):
    ...


class P2SHLitecoinTestnetAddress(P2SHCoinAddressCommon,
                                 CBase58LitecoinTestnetAddress):
    base58_prefix = bytes([58])


class P2SHLitecoinTestnetLegacyAddress(P2SHCoinAddressCommon,
                                       CBase58LitecoinTestnetAddress):
    base58_prefix = bytes([196])


class P2PKHLitecoinTestnetAddress(P2PKHCoinAddressCommon,
                                  CBase58LitecoinTestnetAddress):
    base58_prefix = bytes([111])


class P2SHLitecoinRegtestAddress(P2SHCoinAddressCommon,
                                 CBase58LitecoinRegtestAddress):
    base58_prefix = bytes([58])


class P2SHLitecoinRegtestLegacyAddress(P2SHCoinAddressCommon,
                                       CBase58LitecoinRegtestAddress):
    base58_prefix = bytes([196])


class P2PKHLitecoinRegtestAddress(P2PKHCoinAddressCommon,
                                  CBase58LitecoinRegtestAddress):
    base58_prefix = bytes([111])


class P2WSHLitecoinTestnetAddress(P2WSHCoinAddressCommon,
                                  CBech32LitecoinTestnetAddress):
    ...


class P2WPKHLitecoinTestnetAddress(P2WPKHCoinAddressCommon,
                                   CBech32LitecoinTestnetAddress):
    ...


class P2WSHLitecoinRegtestAddress(P2WSHCoinAddressCommon,
                                  CBech32LitecoinRegtestAddress):
    ...


class P2WPKHLitecoinRegtestAddress(P2WPKHCoinAddressCommon,
                                   CBech32LitecoinRegtestAddress):
    ...


class CLitecoinKey(CBase58CoinKeyBase,
                   metaclass=LitecoinWalletIdentityMeta):
    base58_prefix = bytes([176])


class CLitecoinTestnetKey(CBase58CoinKeyBase,
                          metaclass=LitecoinTestnetWalletIdentityMeta):
    base58_prefix = bytes([239])


class CLitecoinRegtestKey(CBase58CoinKeyBase,
                          metaclass=LitecoinRegtestWalletIdentityMeta):
    base58_prefix = bytes([239])


class CLitecoinExtPubKey(CBase58CoinExtPubKeyBase,
                         metaclass=LitecoinWalletIdentityMeta):
    base58_prefix = b'\x04\x88\xB2\x1E'


class CLitecoinExtKey(CBase58CoinExtKeyBase,
                      metaclass=LitecoinWalletIdentityMeta):
    base58_prefix = b'\x04\x88\xAD\xE4'


class CLitecoinTestnetExtPubKey(CBase58CoinExtPubKeyBase,
                                metaclass=LitecoinTestnetWalletIdentityMeta):
    base58_prefix = b'\x04\x35\x87\xCF'


class CLitecoinTestnetExtKey(CBase58CoinExtKeyBase,
                             metaclass=LitecoinTestnetWalletIdentityMeta):
    base58_prefix = b'\x04\x35\x83\x94'


class CLitecoinRegtestExtPubKey(CBase58CoinExtPubKeyBase,
                                metaclass=LitecoinRegtestWalletIdentityMeta):
    base58_prefix = b'\x04\x35\x87\xCF'


class CLitecoinRegtestExtKey(CBase58CoinExtKeyBase,
                             metaclass=LitecoinRegtestWalletIdentityMeta):
    base58_prefix = b'\x04\x35\x83\x94'


LitecoinWalletIdentityMeta.set_classmap({
    CCoinAddress: CLitecoinAddress,
    CBase58CoinAddress: CBase58LitecoinAddress,
    CBech32CoinAddress: CBech32LitecoinAddress,
    P2SHCoinAddress: P2SHLitecoinAddress,
    P2PKHCoinAddress: P2PKHLitecoinAddress,
    P2WSHCoinAddress: P2WSHLitecoinAddress,
    P2WPKHCoinAddress: P2WPKHLitecoinAddress,
    CCoinKey: CLitecoinKey,
    CCoinExtKey: CLitecoinExtKey,
    CCoinExtPubKey: CLitecoinExtPubKey,
})

LitecoinTestnetWalletIdentityMeta.set_classmap({
    CCoinAddress: CLitecoinTestnetAddress,
    CBase58CoinAddress: CBase58LitecoinTestnetAddress,
    CBech32CoinAddress: CBech32LitecoinTestnetAddress,
    P2SHCoinAddress: P2SHLitecoinTestnetAddress,
    P2PKHCoinAddress: P2PKHLitecoinTestnetAddress,
    P2WSHCoinAddress: P2WSHLitecoinTestnetAddress,
    P2WPKHCoinAddress: P2WPKHLitecoinTestnetAddress,
    CCoinKey: CLitecoinTestnetKey,
    CCoinExtKey: CLitecoinTestnetExtKey,
    CCoinExtPubKey: CLitecoinTestnetExtPubKey,
})

LitecoinRegtestWalletIdentityMeta.set_classmap({
    CCoinAddress: CLitecoinRegtestAddress,
    CBase58CoinAddress: CBase58LitecoinRegtestAddress,
    CBech32CoinAddress: CBech32LitecoinRegtestAddress,
    P2SHCoinAddress: P2SHLitecoinRegtestAddress,
    P2PKHCoinAddress: P2PKHLitecoinRegtestAddress,
    P2WSHCoinAddress: P2WSHLitecoinRegtestAddress,
    P2WPKHCoinAddress: P2WPKHLitecoinRegtestAddress,
    CCoinKey: CLitecoinRegtestKey,
    CCoinExtKey: CLitecoinRegtestExtKey,
    CCoinExtPubKey: CLitecoinRegtestExtPubKey,
})

__all__ = (
    'CLitecoinAddress',
    'CLitecoinTestnetAddress',
    'CBase58LitecoinAddress',
    'CBech32LitecoinAddress',
    'P2SHLitecoinAddress',
    'P2SHLitecoinLegacyAddress',
    'P2PKHLitecoinAddress',
    'P2WSHLitecoinAddress',
    'P2WPKHLitecoinAddress',
    'CBase58LitecoinTestnetAddress',
    'CBech32LitecoinTestnetAddress',
    'P2SHLitecoinTestnetAddress',
    'P2PKHLitecoinTestnetAddress',
    'P2WSHLitecoinTestnetAddress',
    'P2WPKHLitecoinTestnetAddress',
    'CLitecoinKey',
    'CLitecoinExtKey',
    'CLitecoinExtPubKey',
    'CLitecoinTestnetKey',
    'CLitecoinTestnetExtKey',
    'CLitecoinTestnetExtPubKey',
    'CLitecoinRegtestKey',
    'CLitecoinRegtestExtKey',
    'CLitecoinRegtestExtPubKey',
)
