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

from bitcointx.core import (
    CoinTransactionIdentityMeta,
    COutPointBase, CTxWitnessBase, CTxInWitnessBase, CTxOutWitnessBase,
    CTxInBase, CTxOutBase, CTransactionBase,

    CTransaction, CTxIn, CTxOut, CTxWitness, CTxInWitness, CTxOutWitness,
    CMutableTransaction, CMutableTxIn, CMutableTxOut, CMutableTxWitness,
    CMutableTxInWitness, CMutableTxOutWitness, COutPoint, CMutableOutPoint
)
from bitcointx.core.serialize import MutableSerializableMeta
from bitcointx.core.script import CScript
from litecointx.core.script import CLitecoinScript


class LitecoinTransactionIdentityMeta(CoinTransactionIdentityMeta):
    @classmethod
    def _get_extra_classmap(cls):
        return {CScript: CLitecoinScript}


class LitecoinMutableTransactionIdentityMeta(LitecoinTransactionIdentityMeta,
                                             MutableSerializableMeta):
    ...


class CLitecoinOutPoint(COutPointBase,
                        metaclass=LitecoinTransactionIdentityMeta):
    """Litecoin COutPoint"""
    __slots__ = []


class CLitecoinMutableOutPoint(CLitecoinOutPoint,
                               metaclass=LitecoinMutableTransactionIdentityMeta):
    """A mutable Litecoin COutPoint"""
    __slots__ = []


class CLitecoinTxIn(CTxInBase, metaclass=LitecoinTransactionIdentityMeta):
    """An immutable Litecoin TxIn"""
    __slots__ = []


class CLitecoinMutableTxIn(CLitecoinTxIn,
                           metaclass=LitecoinMutableTransactionIdentityMeta):
    """A mutable Litecoin TxIn"""
    __slots__ = []


class CLitecoinTxOut(CTxOutBase, metaclass=LitecoinTransactionIdentityMeta):
    """A immutable Litecoin TxOut"""
    __slots__ = []


class CLitecoinMutableTxOut(CLitecoinTxOut,
                            metaclass=LitecoinMutableTransactionIdentityMeta):
    """A mutable Litecoin CTxOut"""
    __slots__ = []


class CLitecoinTxInWitness(CTxInWitnessBase,
                           metaclass=LitecoinTransactionIdentityMeta):
    """Immutable Litecoin witness data for a single transaction input"""
    __slots__ = []


class CLitecoinMutableTxInWitness(CLitecoinTxInWitness,
                                  metaclass=LitecoinMutableTransactionIdentityMeta):
    """Mutable Litecoin witness data for a single transaction input"""
    __slots__ = []


class _CLitecoinDummyTxOutWitness(CTxOutWitnessBase,
                                  metaclass=LitecoinTransactionIdentityMeta):
    pass


class CLitecoinTxWitness(CTxWitnessBase,
                         metaclass=LitecoinTransactionIdentityMeta):
    """Immutable witness data for all inputs to a transaction"""
    __slots__ = []


class CLitecoinMutableTxWitness(CLitecoinTxWitness,
                                metaclass=LitecoinMutableTransactionIdentityMeta):
    """Witness data for all inputs to a transaction, mutable version"""
    __slots__ = []


class CLitecoinMutableTransaction(CTransactionBase,
                                  metaclass=LitecoinMutableTransactionIdentityMeta):
    """Litecoin transaction"""
    __slots__ = []


class CLitecoinTransaction(CTransactionBase,
                           metaclass=LitecoinTransactionIdentityMeta):
    """Litecoin transaction, mutable version"""
    __slots__ = []


LitecoinTransactionIdentityMeta.set_classmap({
    CTransaction: CLitecoinTransaction,
    CTxIn: CLitecoinTxIn,
    CTxOut: CLitecoinTxOut,
    CTxWitness: CLitecoinTxWitness,
    CTxInWitness: CLitecoinTxInWitness,
    CTxOutWitness: _CLitecoinDummyTxOutWitness,
    COutPoint: CLitecoinOutPoint,
})

LitecoinMutableTransactionIdentityMeta.set_classmap({
    CMutableTransaction: CLitecoinMutableTransaction,
    CMutableTxIn: CLitecoinMutableTxIn,
    CMutableTxOut: CLitecoinMutableTxOut,
    CMutableTxWitness: CLitecoinMutableTxWitness,
    CMutableTxInWitness: CLitecoinMutableTxInWitness,
    CMutableTxOutWitness: _CLitecoinDummyTxOutWitness,
    CMutableOutPoint: CLitecoinMutableOutPoint,
})

LitecoinMutableTransactionIdentityMeta.set_mutable_immutable_links(
    LitecoinTransactionIdentityMeta)

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
