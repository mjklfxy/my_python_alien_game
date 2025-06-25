# My Python Alien Game

这是一个使用Python编写的外星人射击游戏，玩家可以控制飞船进行移动和射击，躲避并击败不断进攻的外星人。

## 📦 项目功能
- 玩家控制飞船进行左右移动
- 玩家可发射子弹击毁外星人
- 外星人自动向下方移动并具有碰撞检测机制
- 游戏包含计分系统与游戏结束逻辑

## 🧰 技术栈
- Python 3.x
- `pygame` 库（用于图形界面和游戏逻辑）

## 📦 安装依赖
确保你已经安装了 Python 和 pip，然后运行：
```
pip install pygame
```

## ▶️ 运行游戏
在项目根目录下运行主程序文件：
```
python alien_invasion.py
```

## 📁 项目结构
```
my_python_alien_game/
├── README.md         # 项目说明文档
├── Alien.py          # 外星人类
├── alien_invasion.py # 游戏入口
├── bullet.py         # 子弹类
├── game_stats.py     # 游戏状态统计
├── setting.py        # 配置参数
└── ship.py           # 飞船类
```