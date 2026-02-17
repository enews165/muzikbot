import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("8525288998:AAFjEcjOGNFgVmQDyoj9z4LfF7KtxppkYQc")

async def muzik(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sarki = update.message.text
    dosya = "song"

    await update.message.reply_text("🎵 hazırlanıyor...")

    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "default_search": "ytsearch1",
        "outtmpl": dosya,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "128"
        }]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([sarki])

        await update.message.reply_audio(audio=open("song.mp3","rb"), title=sarki)
        os.remove("song.mp3")

    except Exception as e:
        await update.message.reply_text("❌ Açamadım")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, muzik))
app.run_polling()
