# 修仙秘境

基于 Pixel Dungeon 1.9.1 开发的中国修仙背景像素 Roguelike。保留原版的回合制探索、程序生成关卡和四职业玩法，并持续替换为修仙题材的中文剧情、角色、怪物、物品与界面。

## 构建要求

- JDK 17
- Android SDK Platform 35
- Android Build Tools 35.0.1
- Python 3（仅资源检查需要）

项目已包含 Gradle 8.9 Wrapper，无需单独安装 Gradle。首次构建前，将 `local.properties` 中的 `sdk.dir` 设置为本机 Android SDK 路径。

## 检查与构建

```bash
python3 tools/validate_project.py
./gradlew --no-daemon assembleDebug
```

Windows 可使用 `gradlew.bat --no-daemon assembleDebug`。

构建产物：`build/outputs/apk/debug/PixelDungeon-debug.apk`。最低支持 Android 5.0（API 21）。

## 项目结构

- `src/`：游戏逻辑、渲染、界面及中文文本
- `assets/`：像素资源、音频和中文字符集
- `res/`：Android 应用名称、图标等资源
- `tools/`：字符集、美术和资源检查脚本

## 版权

本项目基于 [Pixel Dungeon](https://github.com/watabou/pixel-dungeon)，遵循 GNU GPL v3。原项目版权与许可证见 `LICENSE.txt` 及源文件头部。
