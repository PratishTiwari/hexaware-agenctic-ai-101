import os
import gradio as gr
from httpx import AsyncClient
from agent_framework import FunctionInvocationContext, MCPStreamableHTTPTool, Message
from _maf import BACKEND, MODEL, banner, get_client

banner("File -10 - GH MCP Client")

URL = "https://api.githubopilot,com/mcp"
TOKEN = os.environ.get("GITHUB_PERSONAL_ACCESS_TOEKN", "")
if not TOKEN:
    raise SystemExit("Set GITHUB_PERSONAL_ACCESS_TOEKN in .env before running this app.")

READ = ["get_me", "search_repositories", "get_file_contents", "list_commits"]
WRITE = ["create_repository", "create_or_update_file", "delete_file"]
ALLOWED = READ + WRITE
INSTRUCTIONS = ("You are a GitHub assistant. Use the tools for anything about "
                "GitHub - never guess a name or a number. You CAN create "
                "repositories and create or delete files; do it when asked, "
                "then say what you did. Answer in a few lines.")