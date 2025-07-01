from smolagents import (CodeAgent, 
                        GradioUI, 
                        LiteLLMModel, 
                        OpenAIServerModel,
                        LiteLLMRouterModel, 
                        ChatMessage, 
                        ToolCallingAgent)
from smolagents.default_tools import (DuckDuckGoSearchTool, 
                                      VisitWebpageTool, 
                                      WikipediaSearchTool, 
                                      SpeechToTextTool,
                                      PythonInterpreterTool)
import yaml
from tools import (
wikipedia_search,
download_youtube_audio,
transcribe_audio,
analyze_chess_board,
visit_webpage,
read_file,
read_excel_file,
word_reversal,
read_image,
delay_execution_10

)
import os
from dotenv import load_dotenv
import time
from smolagents.default_tools import (DuckDuckGoSearchTool, 
                                      VisitWebpageTool, 
                                      WikipediaSearchTool, 
                                      SpeechToTextTool,
                                      PythonInterpreterTool)
load_dotenv()


model = LiteLLMModel(
    model_id="gemini/gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"), max_tokens=8096,
    fallbacks=["gemini/gemini-2.0-flash", "gemini-2.5-flash-lite-preview-06-17", "gemini/gemini-2.0-flash-lite"],
    timeout=40,
    num_retries=2,
)


agent = CodeAgent(
    model=model,
    tools=[DuckDuckGoSearchTool(),
           wikipedia_search,
        download_youtube_audio,
        transcribe_audio,
        analyze_chess_board,
        visit_webpage,
        read_file,
        read_excel_file,
        word_reversal,
        read_image],
    name="agent",
    description="""
    A smart agent that can answer questions or riddles by creating a plan and executing it step by step. Provide the answer no explanations.
    If the question asks you to not use abbrevations, do not use them.
    """,
    additional_authorized_imports=[
        "*",
        "pandas"
    ],
    max_steps=6,
    verbosity_level=2,
    step_callbacks=[delay_execution_10],
    add_base_tools=True
)



if __name__ == "__main__":
    GradioUI(agent).launch()