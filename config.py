TOKEN = "1870861195:AAGXoP79coilpQ87ErqudRhzcApP4OUjo7M"

# 频率限制次数，每个群每小时内，只能主动触发2次任务
LIMIT_COUNT = 2

# 私有模式，仅授权群组可用  False:关闭    True:打开
EXCLUSIVE_MODE = False

# 配置私有模式群组id列表（不私有请忽略） 例如：[-1001324252532, -100112415423]
EXCLUSIVE_LIST = []

# 主动触发命令仅管理员有效  False:否     True:是
RANK_COMMAND_MODE = True

# 中文字体路径
FRONT = 'fonts/ZhuZiAWan-2.ttc'

# Redis 配置
REDIS_CONFIG = {'host': '127.0.0.1', 'port': 6379, 'db': 1}

# 拥有者 id 配置
OWNER = 1874185094

# 日志频道 id 0 为不启用
CHANNEL = 0

# 帮助信息
HELP = '<b>Group Word Cloud Bot</b>\n\n/start - 查看此帮助信息\n/ping - 我还活着吗？\n/rank - 手动生成词云（绒布球）\n' \
       '/stat - 生成单用户词云\n\n' \
