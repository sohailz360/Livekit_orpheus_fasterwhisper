from livekit.plugins import (
    openai,
    cartesia,
    deepgram,
    silero,
)


import os
import logging
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent

from tts.tts import TTS
from livekit.plugins.google import LLM
from livekit.plugins import deepgram, silero,openai
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv()

# Setup logger
logger = logging.getLogger("voice-agent")
logger.setLevel(logging.DEBUG)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# Load system prompt from file
SYSTEM_PROMPT_PATH = os.path.join(os.path.dirname(__file__), "tara_system_prompt.txt")
with open(SYSTEM_PROMPT_PATH, "r") as f:
    SYSTEM_PROMPT = f.read()

class Assistant(Agent):
    def __init__(self):
        super().__init__(instructions=SYSTEM_PROMPT)

async def entrypoint(ctx: agents.JobContext):
    logger.info(f"connecting to room {ctx.room.name}")
    await ctx.connect()

    logger.info("creating chat context with system prompt")
    # chat_ctx = agents.llm.ChatContext().append(
    #     role="system",
    #     text=SYSTEM_PROMPT,
    # )

    session = AgentSession(
        #stt=openai.STT.with_groq(),

        stt=deepgram.STT(model="nova-3", language="multi"),
        llm=LLM(model="gemini-2.0-flash", temperature=0.4, vertexai=True),
        tts=TTS.create_orpheus_client(),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    logger.info("starting assistant session")
    await session.start(room=ctx.room, agent=Assistant())
    await session.generate_reply(instructions="Greet the user and offer your assistance.")

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))