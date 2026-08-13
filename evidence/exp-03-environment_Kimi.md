# Read-Only Map: Open-LLM-VTuber

## 1. Entry Point Server

**File:** `run_server.py` (root directory)
**Role:** Main entry point for the WebSocket server. Orchestrates:
- Logger initialization
- Frontend submodule check
- Configuration loading via `upgrade_manager.sync_user_config()`
- WebSocketServer instantiation
- Uvicorn server startup

**Key imports:**
- `WebSocketServer` from `src/open_llm_vtuber/server.py`
- `Config`, `read_yaml`, `validate_config` from `src/open_llm_vtuber/config_manager`

---

## 2. WebSocket Routing и Conversation Orchestration

**Primary Files:**

| File | Role |
|------|------|
| `src/open_llm_vtuber/server.py` | FastAPI WebSocketServer class - creates app, mounts routes, static files |
| `src/open_llm_vtuber/routes.py` | Route definitions - `/client-ws`, `/proxy-ws`, `/tts-ws`, `/web-tool`, `/asr` |
| `src/open_llm_vtuber/websocket_handler.py` | WebSocketHandler class - message routing, client management, group operations |
| `src/open_llm_vtuber/message_handler.py` | Message handling logic |
| `src/open_llm_vtuber/chat_group.py` | ChatGroupManager - multi-client group conversation orchestration |
| `src/open_llm_vtuber/chat_history_manager.py` | Chat history persistence |

**Routing Flow:**
```
run_server.py → WebSocketServer.__init__() → routes.init_client_ws_route()
    → WebSocketHandler → _route_message() → _message_handlers dict
    → handle_conversation_trigger() → process_single_conversation() / process_group_conversation()
```

---

## 3. Agent Factory и Stateless LLM Factory

**Files:**

| File | Role |
|------|------|
| `src/open_llm_vtuber/agent/agent_factory.py` | AgentFactory.create_agent() - creates BasicMemoryAgent, Mem0Agent, LettaAgent, HumeAIAgent |
| `src/open_llm_vtuber/agent/stateless_llm_factory.py` | LLMFactory.create_llm() - creates OpenAICompatibleLLM, OllamaLLM, ClaudeLLM, LlamaLLM |
| `src/open_llm_vtuber/agent/agents/agent_interface.py` | AgentInterface ABC |
| `src/open_llm_vtuber/agent/agents/basic_memory_agent.py` | BasicMemoryAgent - main agent with memory, tool support, interrupt handling |
| `src/open_llm_vtuber/agent/stateless_llm/stateless_llm_interface.py` | StatelessLLMInterface ABC |
| `src/open_llm_vtuber/agent/stateless_llm/openai_compatible_llm.py` | OpenAICompatibleLLM implementation |

**Factory Chain:**
```
AgentFactory.create_agent()
    → LLMFactory.create_llm() → StatelessLLMInterface implementations
    → BasicMemoryAgent.__init__() → _set_llm() → _chat_function_factory()
```

---

## 4. OpenAI-Compatible LLM Implementation

**File:** `src/open_llm_vtuber/agent/stateless_llm/openai_compatible_llm.py`
**Role:** AsyncLLM class implementing StatelessLLMInterface
- Uses `openai.AsyncOpenAI` client
- Supports streaming chat completions
- Handles tool calls (OpenAI format)
- Error handling for APIConnectionError, RateLimitError, APIError
- Auto-disables tool support if model doesn't support tools

---

## 5. Config Manager и Оба Default YAML Template

**Files:**

| File | Role |
|------|------|
| `src/open_llm_vtuber/config_manager/__init__.py` | Package exports |
| `src/open_llm_vtuber/config_manager/main.py` | Config class (Pydantic model) |
| `src/open_llm_vtuber/config_manager/system.py` | SystemConfig - host, port, config_alts_dir, tool_prompts |
| `src/open_llm_vtuber/config_manager/character.py` | CharacterConfig - persona_prompt, live2d_model_name, asr_config, tts_config, agent_config |
| `src/open_llm_vtuber/config_manager/utils.py` | read_yaml(), validate_config(), save_config(), scan_config_alts_directory() |
| `src/open_llm_vtuber/config_manager/asr.py` | ASRConfig and provider-specific configs |
| `src/open_llm_vtuber/config_manager/tts.py` | TTSConfig and provider-specific configs |
| `src/open_llm_vtuber/config_manager/agent.py` | AgentConfig, AgentSettings, BasicMemoryAgentConfig |
| `src/open_llm_vtuber/config_manager/vad.py` | VADConfig |
| `src/open_llm_vtuber/config_manager/tts_preprocessor.py` | TTSPreprocessorConfig, TranslatorConfig |
| `src/open_llm_vtuber/config_manager/stateless_llm.py` | OpenAICompatibleConfig, ClaudeConfig, LlamaCppConfig |
| `src/open_llm_vtuber/config_manager/live.py` | LiveConfig, BiliBiliLiveConfig |
| `src/open_llm_vtuber/config_manager/i18n.py` | I18nMixin, MultiLingualString |

**YAML Templates:**

| Template | Path | Role |
|----------|------|------|
| Default (English) | `config_templates/conf.default.yaml` | Main config with English prompts, edge_tts voice |
| Chinese Default | `config_templates/conf.ZH.default.yaml` | Chinese-optimized config, Chinese TTS voice, Chinese ASR |

---

## 6. ASR и TTS Factories

**ASR Factory:**

| File | Role |
|------|------|
| `src/open_llm_vtuber/asr/asr_factory.py` | ASRFactory.get_asr_system() - returns ASRInterface implementation |
| `src/open_llm_vtuber/asr/asr_interface.py` | ASRInterface ABC |
| `src/open_llm_vtuber/asr/faster_whisper_asr.py` | FasterWhisperASR |
| `src/open_llm_vtuber/asr/whisper_cpp_asr.py` | WhisperCPPASR |
| `src/open_llm_vtuber/asr/openai_whisper_asr.py` | WhisperASR |
| `src/open_llm_vtuber/asr/fun_asr.py` | FunASR |
| `src/open_llm_vtuber/asr/azure_asr.py` | AzureASR |
| `src/open_llm_vtuber/asr/groq_whisper_asr.py` | GroqWhisperASR |
| `src/open_llm_vtuber/asr/sherpa_onnx_asr.py` | SherpaOnnxASR |

**TTS Factory:**

| File | Role |
|------|------|
| `src/open_llm_vtuber/tts/tts_factory.py` | TTSFactory.get_tts_engine() - returns TTSInterface implementation |
| `src/open_llm_vtuber/tts/tts_interface.py` | TTSInterface ABC |
| `src/open_llm_vtuber/tts/azure_tts.py` | AzureTTSEngine |
| `src/open_llm_vtuber/tts/edge_tts.py` | EdgeTTSEngine |
| `src/open_llm_vtuber/tts/bark_tts.py` | BarkTTSEngine |
| `src/open_llm_vtuber/tts/cosyvoice_tts.py` | CosyvoiceTTSEngine |
| `src/open_llm_vtuber/tts/cosyvoice2_tts.py` | Cosyvoice2TTSEngine |
| `src/open_llm_vtuber/tts/elevenlabs_tts.py` | ElevenLabsTTSEngine |
| `src/open_llm_vtuber/tts/cartesia_tts.py` | CartesiaTTSEngine |
| `src/open_llm_vtuber/tts/minimax_tts.py` | MinimaxTTSEngine |
| `src/open_llm_vtuber/tts/piper_tts.py` | PiperTTSEngine |
| `src/open_llm_vtuber/tts/siliconflow_tts.py` | SiliconFlowTTS |
| `src/open_llm_vtuber/tts/fish_api_tts.py` | FishAPITTSEngine |
| `src/open_llm_vtuber/tts/melo_tts.py` | MeloTTSEngine |
| `src/open_llm_vtuber/tts/coqui_tts.py` | CoquiTTSEngine |
| `src/open_llm_vtuber/tts/x_tts.py` | XTTSEngine |
| `src/open_llm_vtuber/tts/gpt_sovits_tts.py` | GPTSoVITSConfig |
| `src/open_llm_vtuber/tts/openai_tts.py` | OpenAITTSEngine |
| `src/open_llm_vtuber/tts/sherpa_onnx_tts.py` | SherpaOnnxTTSEngine |
| `src/open_llm_vtuber/tts/pyttsx3_tts.py` | Pyttsx3TTSEngine |
| `src/open_llm_vtuber/tts/spark_tts.py` | SparkTTSEngine |

---

## 7. Frontend Submodule

**Path:** `frontend/`
**Structure:**
```
frontend/
├── index.html              # Entry HTML - loads main-nu7uwxNJ.js and main-QEkl09-0.css
├── assets/                 # Bundled JS and CSS (Vite build output)
└── libs/                   # Potentially vendor libraries
.gitmodules                 # Frontend is a Git submodule
```

**Note:** Frontend is a Git submodule managed by Vite. The `run_server.py` checks if the submodule is initialized and attempts to initialize it if missing.

**Web Tool (separate from frontend):**
- `web_tool/index.html` - Web tool interface
- `web_tool/main.js` - Web tool logic
- `web_tool/recorder.js` - Audio recording utilities

---

## 8. Lint, Pre-commit и CI

**Files:**

| File | Role |
|------|------|
| `.pre-commit-config.yaml` | Pre-commit hooks: ruff (lint), ruff-format (format) |
| `.github/workflows/ruff.yml` | GitHub Actions CI - runs on push/PR |
| `pyproject.toml` | Ruff configuration: target-version = "py310" |

**Lint Stack:**
- **Ruff** (v0.9.6+) - Python linter and formatter
- **Pre-commit** - Local git hook manager
- **GitHub Actions** - CI on push/PR events

---

## 5 Архитектурных Рисков для Локального Agent Gateway

1. **Stateless LLM Factory Single Point of Failure**
   - `LLMFactory.create_llm()` delegates all LLM creation to `OpenAICompatibleLLM` for most providers
   - If OpenAI-compatible endpoint is unreachable, all LLM operations fail
   - No built-in fallback mechanism between providers

2. **Configuration Merge Complexity**
   - `handle_config_switch()` in `service_context.py` uses `deep_merge()` for character config alternatives
   - Risk of partial config updates causing inconsistent state
   - No validation after merge before `load_from_config()`

3. **WebSocket Connection State Management**
   - `WebSocketHandler` maintains in-memory state: `client_connections`, `client_contexts`, `received_data_buffers`, `current_conversation_tasks`
   - Process crash or restart loses all active sessions
   - No persistence layer for active conversations

4. **ASR/TTS Factory Synchronous Initialization**
   - `ASRFactory.get_asr_system()` and `TTSFactory.get_tts_engine()` perform lazy imports
   - Model loading failures only surface at runtime when ASR/TTS is first used
   - No pre-flight validation of model availability

5. **MCP (Model Context Protocol) Integration Complexity**
   - MCP components (`ServerRegistry`, `ToolAdapter`, `ToolManager`, `MCPClient`, `ToolExecutor`) add significant complexity
   - `prompt_mode_flag` in BasicMemoryAgent enables fallback tool calling via JSON detection
   - Risk of race conditions between MCP initialization and agent chat loops
   - Missing `ToolExecutor` leads to silent tool call failures with only warning logs

---

## Summary

| Component | Key File | Risk Level |
|-----------|----------|------------|
| Entry Point | `run_server.py` | Low |
| WebSocket | `websocket_handler.py`, `routes.py` | Medium |
| Agent Factory | `agent_factory.py` | Medium |
| LLM Factory | `stateless_llm_factory.py` | High |
| OpenAI LLM | `openai_compatible_llm.py` | Medium |
| Config Manager | `config_manager/*.py` | Medium |
| YAML Templates | `config_templates/*.yaml` | Low |
| ASR Factory | `asr/asr_factory.py` | Medium |
| TTS Factory | `tts/tts_factory.py` | Medium |
| Frontend | `frontend/` (submodule) | Medium |
| Lint/CI | `.pre-commit-config.yaml`, `.github/workflows/ruff.yml` | Low |