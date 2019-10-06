# Copyright (C) 2018 The python-litecointx developers
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

from typing import List, cast

from bitcointx.core import (
    CoreCoinClassDispatcher, CoreCoinClass,

    CTransaction, CTxIn, CTxOut, CTxWitness, CTxInWitness,
    CMutableTransaction, CMutableTxIn, CMutableTxOut, CMutableTxWitness,
    CMutableTxInWitness, COutPoint, CMutableOutPoint
)
from .script import ScriptLitecoinClassDispatcher


class CoreLitecoinClassDispatcher(CoreCoinClassDispatcher,
                                  depends=[ScriptLitecoinClassDispatcher]):
    ...


class CoreLitecoinClass(CoreCoinClass, metaclass=CoreLitecoinClassDispatcher):
    ...


class CLitecoinOutPoint(COutPoint, CoreLitecoinClass):
    """Litecoin COutPoint"""
    __slots__: List[str] = []


class CLitecoinMutableOutPoint(CLitecoinOutPoint, CMutableOutPoint,
                               CoreLitecoinClass, mutable_of=CLitecoinOutPoint):
    """A mutable Litecoin COutPoint"""
    __slots__: List[str] = []


class CLitecoinTxIn(CTxIn, CoreLitecoinClass):
    """An immutable Litecoin TxIn"""
    __slots__: List[str] = []


class CLitecoinMutableTxIn(CLitecoinTxIn, CMutableTxIn, CoreLitecoinClass,
                           mutable_of=CLitecoinTxIn):
    """A mutable Litecoin TxIn"""
    __slots__: List[str] = []


class CLitecoinTxOut(CTxOut, CoreLitecoinClass):
    """A immutable Litecoin TxOut"""
    __slots__: List[str] = []


class CLitecoinMutableTxOut(CLitecoinTxOut, CMutableTxOut, CoreLitecoinClass,
                            mutable_of=CLitecoinTxOut):
    """A mutable Litecoin CTxOut"""
    __slots__: List[str] = []


class CLitecoinTxInWitness(CTxInWitness, CoreLitecoinClass):
    """Immutable Litecoin witness data for a single transaction input"""
    __slots__: List[str] = []


class CLitecoinMutableTxInWitness(CLitecoinTxInWitness, CMutableTxInWitness,
                                  CoreLitecoinClass,
                                  mutable_of=CLitecoinTxInWitness):
    """Mutable Litecoin witness data for a single transaction input"""
    __slots__: List[str] = []


class CLitecoinTxWitness(CTxWitness, CoreLitecoinClass):
    """Immutable witness data for all inputs to a transaction"""
    __slots__: List[str] = []


class CLitecoinMutableTxWitness(CLitecoinTxWitness, CMutableTxWitness,
                                CoreLitecoinClass,
                                mutable_of=CLitecoinTxWitness):
    """Witness data for all inputs to a transaction, mutable version"""
    __slots__: List[str] = []


class CLitecoinTransaction(CTransaction, CoreLitecoinClass):
    """Litecoin transaction, mutable version"""
    __slots__: List[str] = []

    def to_mutable(self) -> 'CLitecoinMutableTransaction':
        return cast('CLitecoinMutableTransaction', super().to_mutable())

    def to_immutable(self) -> 'CLitecoinTransaction':
        return cast('CLitecoinTransaction', super().to_immutable())


class CLitecoinMutableTransaction(CLitecoinTransaction, CMutableTransaction,
                                  CoreLitecoinClass,
                                  mutable_of=CLitecoinTransaction):
    """Litecoin transaction"""
    __slots__: List[str] = []


__all__ = (
    'CLitecoinOutPoint',
    'CLitecoinMutableOutPoint',
    'CLitecoinTxIn',
    'CLitecoinMutableTxIn',
    'CLitecoinTxOut',
    'CLitecoinMutableTxOut',
    'CLitecoinTransaction',
    'CLitecoinMutableTransaction',
    'CLitecoinTxWitness',
    'CLitecoinMutableTxWitness',
    'CLitecoinMutableTxInWitness',
    'CLitecoinTxInWitness',
)
