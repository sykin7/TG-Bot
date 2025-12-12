
# Telegram Ultimate Bot

一个 **工业级终极 Telegram Bot 项目**，集成 GPT 聊天、图像生成、语音识别、文件处理、群管理和定时任务功能，支持 **Docker 部署** 和 **GitHub Actions 自动构建镜像**。  

本 README 提供 **完整操作指南**，配套真实 Telegram 对话示意图，用户一看就懂。

---

## 目录结构

```

TG-Bot/
├─ bot/
├─ config/
├─ temp/
├─ downloads/
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
└─ docs/
└─ images/

```

> `docs/images/` 存放所有操作截图，可替换为你生成或录制的截图。

---

## 1. 功能模块

### 1.1 GPT 聊天

- 用户直接发送文本消息  
- Bot 自动调用 GPT 模型回复  
- 支持多轮对话

**示意图：**

![GPT 聊天示意](docs/images/gpt_chat.png)

**示例操作：**

```

用户: 你好，请帮我写一首五言绝句
Bot: 春风吹柳绿, 江水映天青...

```

---

### 1.2 图像生成

- 命令格式：`/img <关键词>`  
- 默认生成 512x512 图像，可在 `config.yaml` 调整  

**示意图：**

![图像生成示意](docs/images/img_generate.png)

**示例操作：**

```

/img 一只戴帽子的猫

````

Bot 会返回生成的图像。

---

### 1.3 语音识别

- 用户发送语音消息  
- Bot 自动转文字并使用 GPT 回复

**示意图：**

![语音识别示意](docs/images/voice_recognition.png)

---

### 1.4 文件处理

- 支持上传 `.txt`, `.pdf`, `.jpg`, `.png`, `.mp3`, `.ogg` 等文件  
- Bot 保存到 `downloads/` 文件夹并检查安全性  

**示意图：**

![文件上传示意](docs/images/file_upload.png)

---

### 1.5 群管理（管理员专用）

| 命令        | 功能             | 示例                         |
|------------|----------------|----------------------------|
| `/kick`    | 踢出用户         | `/kick 123456789`          |
| `/ban`     | 禁言用户         | `/ban 123456789 60`        |
| `/broadcast` | 群广播消息       | `/broadcast 大家好`         |
| `/blacklist add` | 添加黑名单      | `/blacklist add spam_user` |
| `/blacklist remove` | 移除黑名单   | `/blacklist remove spam_user` |

**示意图：**

![管理员命令示意](docs/images/admin_command.png)

---

### 1.6 定时任务

- 配置在 `config.yaml` 的 `scheduler.tasks`  
- 支持 CRON 表达式  
- Bot 会在指定时间自动发送消息或提醒  

**示意图：**

![定时任务示意](docs/images/scheduler_task.png)

---

## 2. 配置文件

### 2.1 `.env`

```env
BOT_TOKEN=你的TG_BOT_TOKEN
ADMIN_IDS=123456789,987654321
OPENAI_API_KEY=你的OPENAI_API_KEY
REDIS_URL=redis://redis:6379/0
GROUP_WHITELIST=
GROUP_BLACKLIST=
````

### 2.2 `config.yaml`

```yaml
gpt:
  model: gpt-4
  max_tokens: 500
image:
  size: "512x512"
voice:
  language: "auto"
scheduler:
  tasks:
    - name: daily_reminder
      cron: "0 9 * * *"
      message: "每日提醒"
```

---

## 3. Docker / 容器部署

### 3.1 Docker Compose（推荐）

```bash
docker-compose up -d --build
docker logs -f tg_bot_ultimate
```

* Bot 与 Redis 自动启动
* 数据挂载目录：`temp/` 和 `downloads/`
* 自动重启策略：`restart: always`

**示意图：**

![Docker Compose 启动](docs/images/docker_compose.png)

### 3.2 单容器部署

```bash
docker build -t tg_bot_ultimate .
docker run -d --name tg_bot_redis -p 6379:6379 redis:7-alpine
docker run -d \
  --name tg_bot_ultimate \
  --env-file ./config/config.env \
  -v $(pwd)/temp:/app/temp \
  -v $(pwd)/downloads:/app/downloads \
  --link tg_bot_redis:redis \
  tg_bot_ultimate
```

---

## 4. GitHub Actions 自动构建

* Push 或手动触发 workflow 构建 Docker 镜像
* 推送到 GitHub Container Registry：

```
ghcr.io/<用户名>/<仓库名>:latest
ghcr.io/<用户名>/<仓库名>:sha-<commit_sha>
```

**示意图：**

![GitHub Actions](docs/images/github_actions.png)

---

## 5. 日志查看

```bash
docker logs -f tg_bot_ultimate
docker logs -f tg_bot_redis
```

---

## 6. 使用示例

### 启动命令

```
/start
```

### GPT 聊天

```
你好，请帮我写一首五言绝句
```

### 图像生成

```
/img 一只戴帽子的猫
```

### 语音识别

* 发送语音消息
* Bot 自动转文字并回复

### 文件上传

* 上传文件，Bot 保存到 `downloads/`

### 管理员命令

* `/kick <用户ID>`
* `/ban <用户ID> <分钟>`
* `/broadcast <消息>`
* `/blacklist add/remove <用户名>`

### 定时任务

* 配置 CRON 表达式自动发送消息或提醒

---

## 7. 注意事项

1. `.env` 文件敏感信息不要公开
2. 挂载目录权限必须正确
3. Redis 服务必须可用
4. Bot 容器和 Redis 容器最好在同一 Docker 网络中
5. 配置修改后需重启容器

---

## 8. 常见问题

| 问题        | 解决方法                   |
| --------- | ---------------------- |
| Bot 不回复消息 | 检查 BOT_TOKEN 是否正确，查看日志 |
| GPT 回复延迟  | 检查 OpenAI API 是否可用     |
| 图像生成失败    | 检查 OpenAI API Key 是否正确 |
| 语音识别失败    | 检查 `temp/` 文件夹是否存在     |
| 文件无法保存    | 检查 `downloads/` 文件夹权限  |

---

## 9. 贡献指南

* 提交 PR 或 issue
* 可扩展功能：

  * 更多 GPT 模型
  * 自定义图像参数
  * 高级群管理命令
  * 定时任务插件

---

## 10. 许可证

MIT License

