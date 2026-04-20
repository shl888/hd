"""
全自动交易模块

包含两套策略：
- funding: 资金费套利
- spread: 价差套利
"""

from .funding.open import FundingOpen
from .funding.close import FundingClose
from .funding.sltp import FundingSlTp

from .spread.open import SpreadOpen
from .spread.close import SpreadClose
from .spread.sltp import SpreadSlTp

__all__ = [
    'FundingOpen', 'FundingClose', 'FundingSlTp',
    'SpreadOpen', 'SpreadClose', 'SpreadSlTp',
]