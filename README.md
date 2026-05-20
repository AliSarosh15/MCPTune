# MCPTune

MCPTune is an open-source Python framework for generating tool-use fine-tuning datasets from Model Context Protocol (MCP) servers.

The project explores a simple idea: MCP servers already expose structured tool definitions, parameter schemas, and execution interfaces. MCPTune uses this information to automatically construct training data for language models intended to interact reliably with external tools.

The current focus of the project is infrastructure and dataset generation rather than agent orchestration.

## Features

- MCP server abstraction layer
- Mock MCP integration testing
- Synthetic tool-use dataset generation
- Modular training pipeline
- Open-source contributor workflow with CI

## Architecture

MCPTune currently follows a simple staged pipeline:

```text
MCP Discovery
    ↓
Tool Normalization
    ↓
Dataset Generation
    ↓
Training
    ↓
Evaluation
```

The implementation is intentionally modular so that transports, dataset generators, and training backends can evolve independently.

## Current Status

MCPTune is in early development.

The repository currently contains:
- package infrastructure
- continuous integration
- testing framework
- MCP protocol abstraction
- mock MCP server integration
- initial dataset generation pipeline

Training backends and real MCP transports are planned but not yet implemented.

## Installation

```bash
git clone https://github.com/<username>/MCPTune.git

cd MCPTune

pip install -e .[dev]
```

## Development

Run tests:

```bash
pytest
```

Run linting:

```bash
ruff check .
```

## Project Goals

The primary objective of MCPTune is to make MCP-oriented tool-use fine-tuning reproducible and accessible through a lightweight infrastructure layer.

The project is intentionally designed around:
- modularity
- deterministic testing
- transport abstraction
- protocol-aware dataset generation

rather than autonomous agent systems or orchestration frameworks.

## Roadmap

### v0.1
- MCP abstraction layer
- mock server integration
- basic dataset generation
- OpenAI-style export format

### v0.2
- stdio transport support
- HTTP transport support
- schema normalization
- Hugging Face dataset integration

### v0.3
- QLoRA training backend
- evaluation harness
- multi-tool workflow generation

## Contributing

Contributions, issue reports, and design discussions are welcome.

Before opening a pull request:
- run tests locally
- ensure linting passes
- keep changes focused and documented

## License

MIT License.