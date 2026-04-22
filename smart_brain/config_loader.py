"""
配置加载器
==================================================
【文件职责】
专门负责从环境变量读取敏感配置，接收前端解密密码，解密后存入 data_manager

【当前阶段】
暂时不做解密，只读取明文并存入 data_manager

【未来扩展】
等前端解密密码功能完成后，在这里加入解密逻辑
==================================================
"""

import os
import logging

logger = logging.getLogger(__name__)


class ConfigLoader:
    """
    配置加载器
    ==================================================
    负责：
        1. 启动时从环境变量读取配置（明文）
        2. 接收前端发来的解密密码
        3. （未来）用密码解密配置
        4. 存入 data_manager
    ==================================================
    """
    
    def __init__(self, data_manager):
        """
        初始化配置加载器
        
        :param data_manager: DataManager 实例，用于存储配置
        """
        self.data_manager = data_manager
        self.decryption_password = None  # 解密密码（未来使用）
        self._config_loaded = False      # 是否已加载过配置
    
    # ==================== 对外接口 ====================
    
    def load_all(self):
        """
        加载所有配置（启动时调用）
        ==================================================
        从环境变量读取 API 凭证和数据库配置，存入 data_manager
        ==================================================
        """
        if self._config_loaded:
            logger.debug("📋【配置加载器】配置已加载过，跳过")
            return
        
        logger.info("📋【配置加载器】开始加载配置...")
        
        self._load_api_credentials()
        self._load_database_config()
        
        self._config_loaded = True
        logger.info("✅【配置加载器】所有配置加载完成")
    
    def set_decryption_password(self, password: str):
        """
        接收前端发来的解密密码
        ==================================================
        【当前阶段】只保存密码，不做解密
        【未来扩展】收到密码后，重新从环境变量读取密文，解密后更新 data_manager
        ==================================================
        """
        if not password:
            logger.warning("⚠️【配置加载器】收到空的解密密码")
            return
        
        self.decryption_password = password
        logger.info("🔐【配置加载器】解密密码已接收")
        
        # 未来：在这里触发重新加载并解密
        # self._reload_with_decryption()
    
    # ==================== 内部方法 ====================
    
    def _load_api_credentials(self):
        """
        从环境变量加载 API 凭证
        ==================================================
        【当前阶段】直接读取明文
        【未来扩展】如果已有密码，则解密后再存入
        ==================================================
        """
        # 币安 API
        binance_key = os.getenv('BINANCE_API_KEY')
        binance_secret = os.getenv('BINANCE_API_SECRET')
        
        if not binance_key or not binance_secret:
            logger.error("❌【配置加载器】币安 API 凭证不完整，程序将无法正常交易")
        else:
            # 未来：如果 self.decryption_password 存在，则解密
            # binance_key = decrypt(binance_key, self.decryption_password)
            # binance_secret = decrypt(binance_secret, self.decryption_password)
            
            self.data_manager.set_api_credentials('binance', binance_key, binance_secret)
            logger.info("✅【配置加载器】币安 API 凭证已加载")
        
        # OKX API
        okx_key = os.getenv('OKX_API_KEY')
        okx_secret = os.getenv('OKX_API_SECRET')
        okx_passphrase = os.getenv('OKX_API_PASSPHRASE') or os.getenv('OKX_passphrase')
        
        if not okx_key or not okx_secret or not okx_passphrase:
            logger.error("❌【配置加载器】OKX API 凭证不完整，程序将无法正常交易")
            missing = []
            if not okx_key:
                missing.append("OKX_API_KEY")
            if not okx_secret:
                missing.append("OKX_API_SECRET")
            if not okx_passphrase:
                missing.append("OKX_API_PASSPHRASE/OKX_passphrase")
            logger.error(f"   缺失的变量: {', '.join(missing)}")
        else:
            # 未来：如果 self.decryption_password 存在，则解密
            # okx_key = decrypt(okx_key, self.decryption_password)
            # okx_secret = decrypt(okx_secret, self.decryption_password)
            # okx_passphrase = decrypt(okx_passphrase, self.decryption_password)
            
            self.data_manager.set_api_credentials('okx', okx_key, okx_secret, okx_passphrase)
            logger.info("✅【配置加载器】OKX API 凭证已加载")
    
    def _load_database_config(self):
        """
        从环境变量加载数据库配置
        ==================================================
        【当前阶段】直接读取明文
        【未来扩展】如果已有密码，则解密后再存入
        ==================================================
        """
        mongodb_uri = os.getenv('MONGODB_URI')
        
        if not mongodb_uri:
            logger.error("❌【配置加载器】MONGODB_URI 未设置，数据库功能将无法使用")
        else:
            # 未来：如果 self.decryption_password 存在，则解密
            # mongodb_uri = decrypt(mongodb_uri, self.decryption_password)
            
            self.data_manager.set_database_config('mongodb_uri', mongodb_uri)
            logger.info("✅【配置加载器】MongoDB 配置已加载")
    
    # 未来使用的方法
    # def _reload_with_decryption(self):
    #     """用密码解密并重新加载所有配置"""
    #     logger.info("🔄【配置加载器】用密码重新加载配置...")
    #     self._config_loaded = False
    #     self.load_all()