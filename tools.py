import tempfile
import requests
import os

from time import sleep
from urllib.parse import urlparse
from typing import Optional, List


from PIL import Image
from smolagents import CodeAgent, tool, OpenAIServerModel, LiteLLMModel
from dotenv import load_dotenv
import wikipedia
import time
from PIL import Image
import requests
from io import BytesIO
from smolagents.utils import encode_image_base64, make_image_url
from typing import List
from smolagents import ChatMessage, MessageRole
from stockfish import Stockfish
import pandas as pd
import librosa
from whisper.audio import SAMPLE_RATE
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import numpy
import whisper


@tool
def wikipedia_search(query: str) -> str:
    """
    Search Wikipedia for information about a given topic, the query should be a couple of words.
    Args:
        query: The topic to search for
    """
    wikipedia.set_lang("en")
    return wikipedia.page(query).content

def delay_execution_10(pagent, **kwargs) -> bool:
    """
    Delays the execution for 10 seconds.
    """
    time.sleep(10)
    return True

@tool
def visit_webpage(url: str) -> str:
    """
    Visit a webpage and return the content as text
    Args:
        url: The URL of the webpage to visit
    """

    return requests.get(url).text

@tool
def word_reversal(word: str) -> str:
    """
    Reverse a word

    Args:
        word: The word to reverse
    """
    return word[::-1]

@tool
def read_image(image_path: str) -> str:
    """
    Read an image and return the content as text
    Args:
        image_path: The path to the image to read
    """
    return Image.open(image_path).convert("RGB")

@tool
def read_file(file_path: str) -> str:
    """
    Read a file and return the content as text.
    Args:
        file_path: The path to the file to read
    """

    return open(file_path, "r").read()


@tool
def read_excel_file(file_path: str) -> str:
    """
    Read an excel file and return the content as a pandas dataframe.
    Args:
        file_path: The path to the excel file to read
    """
    return pd.read_excel(file_path)

@tool
def download_youtube_audio(url: str) -> str:
    """
    Download an audio file from a YouTube video by providing the URL and saving it to the current directory.
    Args:
        url: The URL of the YouTube video to download
    """
    
    try:
        yt = YouTube(url)

        yt_audio = yt.streams.filter(only_audio=True,).first()
        yt_audio.download(output_path=os.getcwd(), filename=f"youtube_audio.mp3")
        return f"Audio file downloaded successfully named as: youtube_audio.mp3"
    except Exception as e:
        return f"Error downloading audio file: {e}"

@tool
def transcribe_audio(audio_file_path: str) -> str:
    """
    Transcribes an audio file.  Use when you need to process audio data.
    DO NOT use this tool for YouTube video; use the youtube_transcribe tool to process audio data from YouTube.
    Use this tool when you have an audio file in .mp3, .wav, .aac, .ogg, .flac, .m4a, .alac or .wma

    Args:
        audio_file_path: Filepath to the audio file (str)
    """
    model = whisper.load_model("small")
    audio, sr = librosa.load(audio_file_path, sr=SAMPLE_RATE,duration=5.0)
    result = model.transcribe(audio, language="en",beam_size=5, fp16=False)
    return result['text']

@tool 
def analyze_chess_board(image: Image.Image) -> str:
    """
    Read the image of a chess board and return the best next move for the mentioned player.
    this tool only accepts images of chess boards as input as format Image.Image
    Args:
        image: The image of the chess board
    """

    vision_model = LiteLLMModel(
    "gemini/gemini-2.5-flash", api_key=os.getenv("GOOGLE_API_KEY"), max_tokens=8096,
    )

    prompt = f"""
    You are a chess expert. You are given an image of a chess board and  respond with **only** the FEN string, nothing else.".
    If the image shows the board from the perspective of the white player, meaning the white pieces are on the top of the board, return the FEN string with 'w' as the active player.
    If the image shows the board from the perspective of the black player, meaning the black pieces are on the bottom of the board, return the FEN string with 'b' as the active player.
    """

    messages = [
        ChatMessage(
            role=MessageRole.SYSTEM,
            content=(
                prompt
            ),
        ),
        ChatMessage(
            role=MessageRole.USER,
            content="Convert this board to FEN.",
        ),
    ]

    fen_output = vision_model(messages, images=[image]).content.strip()
    print('output from vision model: ', fen_output)

    # Predict the best next move for the mentioned player.
    sf = Stockfish(path="stockfish.exe", parameters={"Threads": 2, "Skill Level": 20})
    sf.set_fen_position(fen_output)
    best = sf.get_best_move_time(500)
    return 'The best move for the mentioned player is: ' + str(best)