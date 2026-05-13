"""LangGraph CLI / LangGraph Platform entrypoint.

Expose the compiled ``TradingAgentsGraph`` as ``graph`` so ``langgraph dev``
(and deploy) can load it via ``langgraph.json``.

Import cost: builds LLMs and compiles the workflow. Ensure ``.env`` has the
provider key your ``DEFAULT_CONFIG`` expects before starting the dev server.
"""

from __future__ import annotations

from pathlib import Path

# Load repo-root `.env` before imports: `langgraph dev` may use a CWD where
# find_dotenv() does not reach this directory, so tradingagents' package
# __init__ dotenv walk can miss keys.
_REPO_ROOT = Path(__file__).resolve().parent
try:
    from dotenv import load_dotenv

    load_dotenv(_REPO_ROOT / ".env", override=False)
except ImportError:
    pass

from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.graph.trading_graph import TradingAgentsGraph

_DEFAULT_ANALYSTS = ["market", "social", "news", "fundamentals"]

_ta = TradingAgentsGraph(
    selected_analysts=_DEFAULT_ANALYSTS,
    config=DEFAULT_CONFIG.copy(),
    debug=False,
)
graph = _ta.graph
