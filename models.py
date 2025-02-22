from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import AsyncOpenAI
import chardet
from pathlib import Path


BOT_TOKEN = "7804006652:AAEqqgm9SBB8YPQEV97iIsjb108N4D6FZQY"
BOT_USERNAME = "@deepseekmodels_bot"
PROXY_URL = "http://127.0.0.1:1093"

client = AsyncOpenAI(base_url="https://ark.cn-beijing.volces.com/api/v3", api_key="afaa0760-916a-474b-a2e1-d2f4771ed8b4")

speech_file_path = Path(__file__).parent / "speech.mp3"



V3 = "ep-20250217092822-zdjbc"
R1 = "ep-20250217093306-sbhrx"
R1_32B = "ep-20250217093306-sbhrx"
R1_7B = "ep-20250219212147-m8tpn"
db_15_Pro = "ep-20250219214616-dmlvj"
db_15_lite = "ep-20250219214749-25cqt"
db_15_Pro_256K = "ep-20250219214837-4dxg7"
db_pro_256K = "ep-20250219214934-khkts"
db_lite_128K = "ep-20250219215035-65m6f"

# 处理命令
def handle_context(contexts):
    str_contexts = ""
    for context in contexts:
        str_contexts += context + " "
    return str_contexts

async def db_15_Pro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取消息
    message = handle_context(context.args)
    print(f"收到消息：{message}")
    stream = await client.chat.completions.create(
        model=db_15_Pro,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]#stream=True,
    )
    await update.message.reply_text(stream.choices[0].message.content)

async def db_15_lite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取消息
    message = handle_context(context.args)
    print(f"收到消息：{message}")
    stream = await client.chat.completions.create(
        model=db_15_lite,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]#stream=True,
    )
    await update.message.reply_text(stream.choices[0].message.content)

async def db_15_Pro_256K(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取消息
    message = handle_context(context.args)
    print(f"收到消息：{message}")
    stream = await client.chat.completions.create(
        model=db_15_Pro_256K,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]#stream=True,
    )
    await update.message.reply_text(stream.choices[0].message.content)

async def db_pro_256K(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取消息
    message = handle_context(context.args)
    print(f"收到消息：{message}")
    stream = await client.chat.completions.create(
        model=db_pro_256K,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]#stream=True,
    )
    await update.message.reply_text(stream.choices[0].message.content)

async def db_lite_128K(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取消息
    message = handle_context(context.args)
    print(f"收到消息：{message}")
    stream = await client.chat.completions.create(
        model=db_lite_128K,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]#stream=True,
    )
    await update.message.reply_text(stream.choices[0].message.content)



# 处理消息
async def R1_dealer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取消息
    message = handle_context(context.args)
    print(f"收到消息：{message}")
    stream = await client.chat.completions.create(
        model=R1,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]#stream=True,
    )
    await update.message.reply_text(stream.choices[0].message.content)

async def V3_dealer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取消息
    message = handle_context(context.args)
    print(f"收到消息：{message}")
    stream = await client.chat.completions.create(
        model=V3,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]#stream=True,
    )
    await update.message.reply_text(stream.choices[0].message.content)

async def R1_32B_dealer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取消息
    message = handle_context(context.args)
    print(f"收到消息：{message}")
    stream = await client.chat.completions.create(
        model=R1_32B,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]#stream=True,
    )
    await update.message.reply_text(stream.choices[0].message.content)

async def R1_7B_dealer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取消息
    message = handle_context(context.args)
    print(f"收到消息：{message}")
    stream = await client.chat.completions.create(
        model=R1_7B,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]#stream=True,
    )
    await update.message.reply_text(stream.choices[0].message.content)

# 错误处理
def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"更新 {update} 导致错误：{context.error}")

if __name__ == "__main__":
    print("启动机器人...")
    
    # 创建应用
    app = Application.builder().token(BOT_TOKEN).proxy(PROXY_URL).build()

    # 添加命令处理器
    app.add_handler(CommandHandler("R1",R1_dealer))
    app.add_handler(CommandHandler("V3",V3_dealer))
    app.add_handler(CommandHandler("R1_32B",R1_32B_dealer))
    app.add_handler(CommandHandler("R1_7B",R1_7B_dealer))
    app.add_handler(CommandHandler("db_15_Pro",db_15_Pro))
    app.add_handler(CommandHandler("db_15_lite",db_15_lite))
    app.add_handler(CommandHandler("db_15_Pro_256K",db_15_Pro_256K))
    app.add_handler(CommandHandler("db_pro_256K",db_pro_256K))
    app.add_handler(CommandHandler("db_lite_128K",db_lite_128K))


    # 添加消息处理器
    #app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # 添加错误处理器
    app.add_error_handler(error_handler)

    # 轮询模式
    print("机器人运行中...")    
    app.run_polling(poll_interval=3)

