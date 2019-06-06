This Python3 library implements support for Litecoin transactions.

It builds on top, and is intended to be used along with python-bitcointx library.

## Requirements

- [python-bitcointx](https://github.com/Simplexum/python-bitcointx) (version >= 1.0.0)

## Usage:

With contextual switch to Litecoin parameters:

```
import os
import litecointx
from bitcointx import ChainParams, CurrentChainParams
from bitcointx.wallet import (
    CCoinKey, CCoinExtKey, P2WPKHCoinAddress, CCoinAddress
)

with ChainParams('litecoin'):
    k = CCoinExtKey.from_seed(os.urandom(32))
    a = P2WPKHCoinAddress.from_pubkey(k.derive_path("m/0h/0h/1").pub)
    print('example {} address: {}'.format(CurrentChainParams().NAME, a))
    assert CCoinAddress(str(a)) == a

```

With global switch to Litecoin parameters:

```
from litecointx import LitecoinMainnetParams
from bitcointx import SelectChainParams

SelectChainParams('litecoin')
# or, using the chain params class directly
SelectChainParams(LitecoinMainnetParams)

```

Without the switch of chain parameters:

```
from litecointx.wallet import P2SHLitecoinLegacyAddress, P2SHLitecoinAddress

legacy_adr = P2SHLitecoinLegacyAddress('3F1c6UWAs9RLN2Mbt5bAJue12VhVCorXzs')
canonical_adr = P2SHLitecoinAddress.from_scriptPubKey(legacy_adr.to_scriptPubKey())
assert str(canonical_adr) == 'MMDkQMv8pGGmAXdVyxaW8YtQMCHw7eouma'

```
