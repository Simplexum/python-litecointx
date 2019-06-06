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

from bitcointx.core.script import CScript, CScriptBase


class CLitecoinScript(CScriptBase):
    ...


# Make CLitecoinScript behave like a a subclass of CScript
# regarding isinstance(script, CScript), etc
CScript.register(CLitecoinScript)
