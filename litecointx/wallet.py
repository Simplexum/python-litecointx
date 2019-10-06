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

from typing import Type, List

from bitcointx import get_current_chain_params
from bitcointx.util import dispatcher_mapped_list, ClassMappingDispatcher
from bitcointx.wallet import (
    WalletCoinClassDispatcher, WalletCoinClass,
    CCoinAddress, P2SHCoinAddress, P2WSHCoinAddress,
    P2PKHCoinAddress, P2WPKHCoinAddress,
    CBase58CoinAddress, CBech32CoinAddress,
    CCoinKey, CCoinExtKey, CCoinExtPubKey,
    T_CBase58DataDispatched
)
from .core import CoreLitecoinClassDispatcher


class WalletLitecoinClassDispatcher(WalletCoinClassDispatcher,
                                    depends=[CoreLitecoinClassDispatcher]):
    ...


class WalletLitecoinTestnetClassDispatcher(WalletLitecoinClassDispatcher):
    ...


class WalletLitecoinRegtestClassDispatcher(WalletLitecoinClassDispatcher):
    ...


class WalletLitecoinClass(WalletCoinClass,
                          metaclass=WalletLitecoinClassDispatcher):
    ...


class WalletLitecoinTestnetClass(
    WalletLitecoinClass, metaclass=WalletLitecoinTestnetClassDispatcher
):
    ...


class WalletLitecoinRegtestClass(
    WalletLitecoinClass, metaclass=WalletLitecoinRegtestClassDispatcher
):
    ...


class CLitecoinAddress(CCoinAddress, WalletLitecoinClass):
    ...


class CLitecoinTestnetAddress(CCoinAddress, WalletLitecoinTestnetClass):
    ...


class CLitecoinRegtestAddress(CCoinAddress, WalletLitecoinRegtestClass):
    ...


class CBase58LitecoinAddress(CBase58CoinAddress, CLitecoinAddress):
    @classmethod
    def base58_get_match_candidates(cls: Type[T_CBase58DataDispatched]
                                    ) -> List[Type[T_CBase58DataDispatched]]:
        assert isinstance(cls, ClassMappingDispatcher)
        candidates = dispatcher_mapped_list(cls)
        if P2SHLitecoinAddress in candidates\
                and get_current_chain_params().allow_legacy_p2sh:
            return [P2SHLitecoinLegacyAddress] + candidates
        return super(CBase58LitecoinAddress, cls).base58_get_match_candidates()


class CBase58LitecoinTestnetAddress(CBase58CoinAddress,
                                    CLitecoinTestnetAddress):
    ...


class CBase58LitecoinRegtestAddress(CBase58CoinAddress,
                                    CLitecoinRegtestAddress):
    ...


class CBech32LitecoinAddress(CBech32CoinAddress, CLitecoinAddress):
    bech32_hrp = 'ltc'


class CBech32LitecoinTestnetAddress(CBech32CoinAddress,
                                    CLitecoinTestnetAddress):
    bech32_hrp = 'tltc'


class CBech32LitecoinRegtestAddress(CBech32CoinAddress,
                                    CLitecoinRegtestAddress):
    bech32_hrp = 'rltc'


class P2SHLitecoinAddress(P2SHCoinAddress, CBase58LitecoinAddress):
    base58_prefix = bytes([50])


class P2SHLitecoinLegacyAddress(P2SHCoinAddress, CBase58LitecoinAddress,
                                variant_of=P2SHLitecoinAddress):
    base58_prefix = bytes([5])


class P2PKHLitecoinAddress(P2PKHCoinAddress, CBase58LitecoinAddress):
    base58_prefix = bytes([48])


class P2WSHLitecoinAddress(P2WSHCoinAddress, CBech32LitecoinAddress):
    ...


class P2WPKHLitecoinAddress(P2WPKHCoinAddress, CBech32LitecoinAddress):
    ...


class P2SHLitecoinTestnetAddress(P2SHCoinAddress,
                                 CBase58LitecoinTestnetAddress):
    base58_prefix = bytes([58])


class P2SHLitecoinTestnetLegacyAddress(P2SHCoinAddress,
                                       CBase58LitecoinTestnetAddress,
                                       variant_of=P2SHLitecoinTestnetAddress):
    base58_prefix = bytes([196])


class P2PKHLitecoinTestnetAddress(P2PKHCoinAddress,
                                  CBase58LitecoinTestnetAddress):
    base58_prefix = bytes([111])


class P2SHLitecoinRegtestAddress(P2SHCoinAddress,
                                 CBase58LitecoinRegtestAddress):
    base58_prefix = bytes([58])


class P2SHLitecoinRegtestLegacyAddress(P2SHCoinAddress,
                                       CBase58LitecoinRegtestAddress,
                                       variant_of=P2SHLitecoinRegtestAddress):
    base58_prefix = bytes([196])


class P2PKHLitecoinRegtestAddress(P2PKHCoinAddress,
                                  CBase58LitecoinRegtestAddress):
    base58_prefix = bytes([111])


class P2WSHLitecoinTestnetAddress(P2WSHCoinAddress,
                                  CBech32LitecoinTestnetAddress):
    ...


class P2WPKHLitecoinTestnetAddress(P2WPKHCoinAddress,
                                   CBech32LitecoinTestnetAddress):
    ...


class P2WSHLitecoinRegtestAddress(P2WSHCoinAddress,
                                  CBech32LitecoinRegtestAddress):
    ...


class P2WPKHLitecoinRegtestAddress(P2WPKHCoinAddress,
                                   CBech32LitecoinRegtestAddress):
    ...


class CLitecoinKey(CCoinKey, WalletLitecoinClass):
    base58_prefix = bytes([176])


class CLitecoinTestnetKey(CCoinKey, WalletLitecoinTestnetClass):
    base58_prefix = bytes([239])


class CLitecoinRegtestKey(CCoinKey, WalletLitecoinRegtestClass):
    base58_prefix = bytes([239])


class CLitecoinExtPubKey(CCoinExtPubKey, WalletLitecoinClass):
    base58_prefix = b'\x04\x88\xB2\x1E'


class CLitecoinExtKey(CCoinExtKey, WalletLitecoinClass):
    base58_prefix = b'\x04\x88\xAD\xE4'


class CLitecoinTestnetExtPubKey(CCoinExtPubKey, WalletLitecoinTestnetClass):
    base58_prefix = b'\x04\x35\x87\xCF'


class CLitecoinTestnetExtKey(CCoinExtKey, WalletLitecoinTestnetClass):
    base58_prefix = b'\x04\x35\x83\x94'


class CLitecoinRegtestExtPubKey(CCoinExtPubKey, WalletLitecoinRegtestClass):
    base58_prefix = b'\x04\x35\x87\xCF'


class CLitecoinRegtestExtKey(CCoinExtKey, WalletLitecoinRegtestClass):
    base58_prefix = b'\x04\x35\x83\x94'


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
