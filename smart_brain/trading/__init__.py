"""
交易逻辑模块

架构说明：
- 大脑直接持有所有工人，不再通过中间层转发
- 半自动工人：leverage_worker, open_worker, sl_tp_worker, close_worker
- 全自动工人：funding 和 spread 两套策略
- 本文件保留用于模块导出，TradingLogic 类已废弃删除
"""

# 半自动工人导出
from .semi_auto.leverage_worker import LeverageWorker
from .semi_auto.open_position_worker import OpenPositionWorker
from .semi_auto.sl_tp_worker import SlTpWorker
from .semi_auto.close_position_worker import ClosePositionWorker

# 全自动工人导出（从子包导入）
from .full_auto.funding import FundingOpen, FundingClose, FundingSlTp
from .full_auto.spread import SpreadOpen, SpreadClose, SpreadSlTp

__all__ = [
    # 半自动
    'LeverageWorker',
    'OpenPositionWorker',
    'SlTpWorker',
    'ClosePositionWorker',
    # 资金费套利
    'FundingOpen',
    'FundingClose',
    'FundingSlTp',
    # 价差套利
    'SpreadOpen',
    'SpreadClose',
    'SpreadSlTp',
]