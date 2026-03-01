接入说明

1) 在项目中安装依赖（建议在虚拟环境中运行）:

```bash
pip install -r integrations/discord_bot/requirements.txt
```

2) 创建 `.env` 文件并设置你的凭证（参照 `.env.example`）:

```text
DISCORD_TOKEN=你的_discord_bot_token
MEMU_API_KEY=你的_memu_api_key
```

3) 运行机器人:

```bash
python integrations/discord_bot/bot.py
```

说明
- 这个示例机器人会把收到的消息调用 `memu` SDK 的 `memorize_conversation` 存入 memU。示例中只做了存储和回执。要让机器人返回 memU 的智能回复，请将注释中标记的 TODO 部分替换为对 memU Response API 或 SDK 的调用（取决于你使用的 memu-py 版本）。
