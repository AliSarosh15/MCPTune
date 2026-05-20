# examples/simple_mcp_server.py

from fastmcp import FastMCP


mcp = FastMCP("mcptune-test-server")


@mcp.tool()
def get_weather(city: str) -> str:
    """
    Get the current weather for a city.
    """
    return f"The weather in {city} is sunny and 22°C."


@mcp.tool()
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def search_docs(query: str) -> str:
    """
    Search project documentation.
    """
    return f"Results for query: {query}"


if __name__ == "__main__":
    mcp.run()