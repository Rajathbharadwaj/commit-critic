"""
LangGraph Platform entry point for Commit Critic.

This module exports the agent graph for use with:
- langgraph dev (development server)
- langgraph up (Docker deployment)
- LangGraph Cloud

Usage:
    langgraph dev  # Start dev server at http://localhost:2024
"""

from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model

from .prompts import MAIN_AGENT_PROMPT, get_date_context
from .subagents import get_commit_critic_subagents
from .tools import get_repo_info_tool


def create_commit_critic_graph(config: dict = None):
    """
    Create the Commit Critic deep agent graph.

    This function is called by LangGraph Platform to instantiate the agent.

    Args:
        config: RunnableConfig dict with optional configurable parameters:
            - model_name: LLM model to use (default: claude-sonnet-4-5-20250929)
            - repo_path: Repository path for analysis (default: current dir)

    Returns:
        CompiledStateGraph - the LangGraph agent ready for invocation
    """
    config = config or {}
    configurable = config.get("configurable", {})

    # Get configuration with defaults
    model_name = configurable.get("model_name", "claude-sonnet-4-5-20250929")
    repo_path = configurable.get("repo_path", ".")

    # Initialize model
    model = init_chat_model(model_name)

    # Build system prompt with date context
    date_context = get_date_context()
    system_prompt = f"{MAIN_AGENT_PROMPT}\n\n{date_context}\n\nDefault repository: {repo_path}"

    # Get subagents
    subagents = get_commit_critic_subagents()

    # Main agent tools (orchestrator level)
    main_tools = [get_repo_info_tool]

    # Create the deep agent graph
    # Note: LangGraph Platform handles checkpointing automatically via store/checkpointer config
    agent = create_deep_agent(
        model=model,
        system_prompt=system_prompt,
        tools=main_tools,
        subagents=subagents,
    )

    return agent


# For direct imports (e.g., testing)
graph = create_commit_critic_graph
