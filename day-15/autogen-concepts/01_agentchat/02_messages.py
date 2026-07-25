import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage, StopMessage, TextMessage
from autogen_core import CancellationToken, Image
from PIL import Image as PILImage
