Windows PowerShell
(C) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

Попробуйте новую кроссплатформенную оболочку PowerShell (https://aka.ms/pscore6)

PS C:\dev\agent-lab\Open-LLM-VTuber> git fetch upstream
From https://github.com/Open-LLM-VTuber/Open-LLM-VTuber
 * [new branch]      dependabot/pip/pip-ec91b00199 -> upstream/dependabot/pip/pip-ec91b00199
 * [new branch]      dependabot/uv/uv-40471c2271 -> upstream/dependabot/uv/uv-40471c2271
 * [new branch]      dev                   -> upstream/dev
 * [new branch]      feat/MemU-integration -> upstream/feat/MemU-integration
 * [new branch]      main                  -> upstream/main
 * [new branch]      sherpa-onnx-gpu-attempt -> upstream/sherpa-onnx-gpu-attempt
 * [new branch]      stream_tts            -> upstream/stream_tts
 * [new branch]      v0.3.0                -> upstream/v0.3.0
 * [new branch]      v1-release            -> upstream/v1-release
 * [new branch]      v2                    -> upstream/v2
 * [new branch]      ylxmf2005-patch-1     -> upstream/ylxmf2005-patch-1
PS C:\dev\agent-lab\Open-LLM-VTuber> git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS C:\dev\agent-lab\Open-LLM-VTuber> git merge --ff-only upstream/main
Already up to date.
PS C:\dev\agent-lab\Open-LLM-VTuber> git push origin main
Everything up-to-date
PS C:\dev\agent-lab\Open-LLM-VTuber> git switch feat/local-agent-gateway
Switched to branch 'feat/local-agent-gateway'
PS C:\dev\agent-lab\Open-LLM-VTuber> git rebase main
Current branch feat/local-agent-gateway is up to date.
PS C:\dev\agent-lab\Open-LLM-VTuber> uv sync
Using CPython 3.10.20
Creating virtual environment at: .venv
Resolved 310 packages in 1ms
      Built langdetect==1.0.9                                                                                           Prepared 96 packages in 26.07s
Installed 123 packages in 2.78s
 + aiohappyeyeballs==2.6.1
 + aiohttp==3.13.3
 + aiosignal==1.4.0
 + annotated-doc==0.0.4
 + annotated-types==0.7.0
 + anthropic==0.76.0
 + anyio==4.12.1
 + async-timeout==5.0.1
 + attrs==25.4.0
 + azure-cognitiveservices-speech==1.47.0
 + azure-core==1.38.0
 + beautifulsoup4==4.14.3
 + cartesia==2.0.17
 + certifi==2026.1.4
 + cffi==2.0.0
 + cfgv==3.5.0
 + chardet==5.2.0
 + charset-normalizer==3.4.4
 + click==8.3.1
 + colorama==0.4.6
 + coloredlogs==15.0.1
 + comtypes==1.4.15
 + cryptography==46.0.3
 + distlib==0.4.0
 + distro==1.9.0
 + dnspython==2.8.0
 + docstring-parser==0.17.0
 + duckduckgo-mcp-server==0.1.1
 + edge-tts==7.2.7
 + elevenlabs==2.31.0
 + email-validator==2.3.0
 + exceptiongroup==1.3.1
 + fastapi==0.128.0
 + fastapi-cli==0.0.20
 + fastapi-cloud-cli==0.11.0
 + fastar==0.8.0
 + filelock==3.20.3
 + flatbuffers==25.12.19
 + frozenlist==1.8.0
 + fsspec==2026.1.0
 + groq==1.0.0
 + h11==0.16.0
 + httpcore==1.0.9
 + httptools==0.7.1
 + httpx==0.28.1
 + httpx-sse==0.4.0
 + humanfriendly==10.0
 + identify==2.6.16
 + idna==3.11
 + iterators==0.2.0
 + jinja2==3.1.6
 + jiter==0.12.0
 + jsonschema==4.26.0
 + jsonschema-specifications==2025.9.1
 + langdetect==1.0.9
 + letta-client==1.7.6
 + loguru==0.7.3
 + markdown-it-py==4.0.0
 + markupsafe==3.0.3
 + mcp==1.26.0
 + mdurl==0.1.2
 + mpmath==1.3.0
 + multidict==6.7.0
 + networkx==3.4.2
 + nodeenv==1.10.0
 + numpy==1.26.4
 + onnxruntime==1.23.2
 + openai==2.15.0
 + packaging==26.0
 + platformdirs==4.5.1
 + pre-commit==4.5.1
 + propcache==0.4.1
 + protobuf==6.33.4
 + pycparser==3.0
 + pydantic==2.12.5
 + pydantic-core==2.41.5
 + pydantic-extra-types==2.11.0
 + pydantic-settings==2.12.0
 + pydub==0.25.1
 + pygments==2.19.2
 + pyjwt==2.10.1
 + pypiwin32==223
 + pyreadline3==3.5.4
 + pysbd==0.3.4
 + python-dotenv==1.2.1
 + python-multipart==0.0.21
 + pyttsx3==2.99
 + pywin32==311
 + pyyaml==6.0.3
 + referencing==0.37.0
 + requests==2.32.5
 + rich==14.3.1
 + rich-toolkit==0.17.1
 + rignore==0.7.6
 + rpds-py==0.30.0
 + ruamel-yaml==0.19.1
 + ruff==0.14.14
 + scipy==1.15.3
 + sentry-sdk==2.50.0
 + shellingham==1.5.4
 + sherpa-onnx==1.10.46
 + six==1.17.0
 + sniffio==1.3.1
 + soundfile==0.13.1
 + soupsieve==2.8.3
 + sse-starlette==3.2.0
 + starlette==0.50.0
 + sympy==1.14.0
 + tabulate==0.9.0
 + tomli==2.4.0
 + torch==2.10.0
 + tqdm==4.67.1
 + typer==0.21.1
 + typing-extensions==4.15.0
 + typing-inspection==0.4.2
 + urllib3==2.6.3
 + uvicorn==0.40.0
 + virtualenv==20.36.1
 + watchfiles==1.1.1
 + websocket-client==1.9.0
 + websockets==16.0
 + win32-setctime==1.2.0
 + yarl==1.22.0
PS C:\dev\agent-lab\Open-LLM-VTuber> Copy-Item config_templates/conf.default.yaml conf.yaml
PS C:\dev\agent-lab\Open-LLM-VTuber> uv run run_server.py --verbose
[INFO] Running in verbose mode
2026-07-29 23:58:29 | INFO     | __main__:run:122 | Open-LLM-VTuber, version v1.2.1
2026-07-29 23:58:29 | INFO     | upgrade_codes.config_sync:backup_user_config:100 | Backing up conf.yaml to conf.yaml.backup
2026-07-29 23:58:29 | DEBUG    | upgrade_codes.config_sync:backup_user_config:105 | Config backup path: C:\dev\agent-lab\Open-LLM-VTuber\conf.yaml.backup
2026-07-29 23:58:29 | INFO     | __main__:run:149 | Initializing server context...
2026-07-29 23:58:29 | INFO     | src.open_llm_vtuber.service_context:init_live2d:315 | Initializing Live2D: mao_pro
2026-07-29 23:58:29 | INFO     | src.open_llm_vtuber.live2d_model:_lookup_model_info:142 | Model Information Loaded.
2026-07-29 23:58:29 | INFO     | src.open_llm_vtuber.service_context:init_asr:325 | Initializing ASR: sherpa_onnx_asr
2026-07-29 23:58:30 | INFO     | src.open_llm_vtuber.asr.sherpa_onnx_asr:__init__:85 | Sherpa-Onnx-ASR: Using cpu for inference
2026-07-29 23:58:30 | WARNING  | src.open_llm_vtuber.asr.sherpa_onnx_asr:_create_recognizer:170 | SenseVoice model not found. Downloading the model...
2026-07-29 23:58:30 | WARNING  | src.open_llm_vtuber.asr.utils:check_and_extract_local_file:160 | Local file not found or not a tar.bz2 archive: models\sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17.tar.bz2
2026-07-29 23:58:30 | INFO     | src.open_llm_vtuber.asr.sherpa_onnx_asr:_create_recognizer:180 | Local file not found. Downloading...
2026-07-29 23:58:30 | INFO     | src.open_llm_vtuber.asr.utils:download_and_extract:82 | 🏃‍♂️Downloading https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17.tar.bz2 to ./models\sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17.tar.bz2...
2026-07-29 23:58:31 | DEBUG    | src.open_llm_vtuber.asr.utils:download_and_extract:86 | Total file size: 999.33 MB
sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17.tar.bz2: 100%|███████████████| 999M/999M [01:02<00:00, 16.9MiB/s]
2026-07-29 23:59:33 | INFO     | src.open_llm_vtuber.asr.utils:download_and_extract:102 | Downloaded sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17.tar.bz2 successfully.
2026-07-29 23:59:33 | INFO     | src.open_llm_vtuber.asr.utils:download_and_extract:106 | Extracting sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17.tar.bz2...
2026-07-30 00:00:26 | INFO     | src.open_llm_vtuber.asr.utils:download_and_extract:109 | Extraction completed.
2026-07-30 00:00:26 | DEBUG    | src.open_llm_vtuber.asr.utils:download_and_extract:113 | Deleted the compressed file: sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17.tar.bz2
2026-07-30 00:00:29 | INFO     | src.open_llm_vtuber.service_context:init_tts:337 | Initializing TTS: edge_tts
2026-07-30 00:00:29 | INFO     | src.open_llm_vtuber.service_context:init_vad:349 | VAD is disabled.
2026-07-30 00:00:29 | INFO     | src.open_llm_vtuber.service_context:load_from_config:286 | Initializing shared ServerRegistry within load_from_config.
2026-07-30 00:00:29 | DEBUG    | src.open_llm_vtuber.mcpp.server_registry:load_servers:91 | MCPSR: Loaded server: 'time'.
2026-07-30 00:00:29 | DEBUG    | src.open_llm_vtuber.mcpp.server_registry:load_servers:91 | MCPSR: Loaded server: 'ddg-search'.
2026-07-30 00:00:29 | INFO     | src.open_llm_vtuber.service_context:load_from_config:290 | Initializing shared ToolAdapter within load_from_config.
2026-07-30 00:00:29 | DEBUG    | src.open_llm_vtuber.service_context:_init_mcp_components:97 | Initializing MCP components: use_mcpp=True, enabled_servers=['time', 'ddg-search']
2026-07-30 00:00:29 | DEBUG    | src.open_llm_vtuber.mcpp.server_registry:load_servers:91 | MCPSR: Loaded server: 'time'.
2026-07-30 00:00:29 | DEBUG    | src.open_llm_vtuber.mcpp.server_registry:load_servers:91 | MCPSR: Loaded server: 'ddg-search'.
2026-07-30 00:00:29 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:112 | ServerRegistry initialized or referenced.
2026-07-30 00:00:29 | INFO     | src.open_llm_vtuber.mcpp.tool_adapter:get_tools:223 | MC: Running dynamic tool construction for servers: ['time', 'ddg-search']
2026-07-30 00:00:29 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:31 | MC: Fetching tool info for enabled servers: ['time', 'ddg-search']
2026-07-30 00:00:29 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:__init__:41 | MCPC: Initialized MCPClient instance.
2026-07-30 00:00:29 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:90 | MCPC: Cache miss for list_tools on server 'time'. Fetching...
2026-07-30 00:00:29 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:50 | MCPC: Starting and connecting to server 'time'...
2026-07-30 00:00:48 | ERROR    | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:78 | MCPC: Failed to connect to server 'time': Connection closed
Traceback (most recent call last):

  File "C:\dev\agent-lab\Open-LLM-VTuber\run_server.py", line 178, in <module>
    run(console_log_level=console_log_level)
    │                     └ 'DEBUG'
    └ <function run at 0x0000027C090DECB0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\run_server.py", line 151, in run
    asyncio.run(server.initialize())
    │       │   │      └ <function WebSocketServer.initialize at 0x0000027C090DE950>
    │       │   └ <src.open_llm_vtuber.server.WebSocketServer object at 0x0000027C09088C70>
    │       └ <function run at 0x0000027C64E70F70>
    └ <module 'asyncio' from 'C:\\Users\\gst\\AppData\\Roaming\\uv\\python\\cpython-3.10-windows-x86_64-none\\lib\\asyncio\\__init_...

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\runners.py", line 44, in run
    return loop.run_until_complete(main)
           │    │                  └ <coroutine object WebSocketServer.initialize at 0x0000027C091F3A70>
           │    └ <function BaseEventLoop.run_until_complete at 0x0000027C64E72950>
           └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 636, in run_until_complete
    self.run_forever()
    │    └ <function ProactorEventLoop.run_forever at 0x0000027C64F263B0>
    └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\windows_events.py", line 321, in run_forever
    super().run_forever()

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 603, in run_forever
    self._run_once()
    │    └ <function BaseEventLoop._run_once at 0x0000027C64E58430>
    └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 1909, in _run_once
    handle._run()
    │      └ <function Handle._run at 0x0000027C64DA3D00>
    └ <Handle Task.task_wakeup(<Future finished result=True>)>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\events.py", line 80, in _run
    self._context.run(self._callback, *self._args)
    │    │            │    │           │    └ <member '_args' of 'Handle' objects>
    │    │            │    │           └ <Handle Task.task_wakeup(<Future finished result=True>)>
    │    │            │    └ <member '_callback' of 'Handle' objects>
    │    │            └ <Handle Task.task_wakeup(<Future finished result=True>)>
    │    └ <member '_context' of 'Handle' objects>
    └ <Handle Task.task_wakeup(<Future finished result=True>)>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\server.py", line 154, in initialize
    await self.default_context_cache.load_from_config(self.config)
          │    │                     │                │    └ Config(system_config=SystemConfig(conf_version='v1.2.1', host='localhost', port=12393, config_alts_dir='characters', tool_pro...
          │    │                     │                └ <src.open_llm_vtuber.server.WebSocketServer object at 0x0000027C09088C70>
          │    │                     └ <function ServiceContext.load_from_config at 0x0000027C08DCD630>
          │    └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C090887C0>
          └ <src.open_llm_vtuber.server.WebSocketServer object at 0x0000027C09088C70>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\service_context.py", line 294, in load_from_config
    await self._init_mcp_components(
          │    └ <function ServiceContext._init_mcp_components at 0x0000027C08DCD480>
          └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C090887C0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\service_context.py", line 127, in _init_mcp_components
    ) = await self.tool_adapter.get_tools(enabled_servers)
              │    │            │         └ ['time', 'ddg-search']
              │    │            └ <function ToolAdapter.get_tools at 0x0000027C078B84C0>
              │    └ <src.open_llm_vtuber.mcpp.tool_adapter.ToolAdapter object at 0x0000027C0893FB20>
              └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C090887C0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\tool_adapter.py", line 226, in get_tools
    servers_info, formatted_tools_dict = await self.get_server_and_tool_info(
                                               │    └ <function ToolAdapter.get_server_and_tool_info at 0x0000027C078B8310>
                                               └ <src.open_llm_vtuber.mcpp.tool_adapter.ToolAdapter object at 0x0000027C0893FB20>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\tool_adapter.py", line 44, in get_server_and_tool_info
    tools = await client.list_tools(server_name)
                  │      │          └ 'time'
                  │      └ <function MCPClient.list_tools at 0x0000027C0655A9E0>
                  └ <src.open_llm_vtuber.mcpp.mcp_client.MCPClient object at 0x0000027C0893C1F0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\mcp_client.py", line 93, in list_tools
    session = await self._ensure_server_running_and_get_session(server_name)
                    │    │                                      └ 'time'
                    │    └ <function MCPClient._ensure_server_running_and_get_session at 0x0000027C0651F400>
                    └ <src.open_llm_vtuber.mcpp.mcp_client.MCPClient object at 0x0000027C0893C1F0>

> File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\mcp_client.py", line 72, in _ensure_server_running_and_get_session
    await session.initialize()
          │       └ <function ClientSession.initialize at 0x0000027C0651F520>
          └ <mcp.client.session.ClientSession object at 0x0000027C0908BCD0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\mcp\client\session.py", line 171, in initialize
    result = await self.send_request(
                   │    └ <function BaseSession.send_request at 0x0000027C0651D240>
                   └ <mcp.client.session.ClientSession object at 0x0000027C0908BCD0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\mcp\shared\session.py", line 306, in send_request
    raise McpError(response_or_error.error)
          │        │                 └ ErrorData(code=-32000, message='Connection closed', data=None)
          │        └ JSONRPCError(jsonrpc='2.0', id=0, error=ErrorData(code=-32000, message='Connection closed', data=None))
          └ <class 'mcp.shared.exceptions.McpError'>

mcp.shared.exceptions.McpError: Connection closed
2026-07-30 00:00:48 | ERROR    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:64 | MC: Failed to get info for server 'time': MCPC: Failed to connect to server 'time'.
2026-07-30 00:00:48 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:90 | MCPC: Cache miss for list_tools on server 'ddg-search'. Fetching...
2026-07-30 00:00:48 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:50 | MCPC: Starting and connecting to server 'ddg-search'...
2026-07-30 00:00:54 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:75 | MCPC: Successfully connected to server 'ddg-search'.
2026-07-30 00:00:54 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:98 | MCPC: Cached list_tools result for server 'ddg-search'.
2026-07-30 00:00:54 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:45 | MC: Found 2 tools on server 'ddg-search'
2026-07-30 00:00:54 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:aclose:159 | MCPC: Closing client instance and 1 active connections...
2026-07-30 00:00:54 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:aclose:166 | MCPC: Client instance closed.
2026-07-30 00:00:54 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:80 | MC: Finished fetching tool info. Found 2 tools across enabled servers.
2026-07-30 00:00:54 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:construct_mcp_prompt_string:96 | MC: Constructing MCP prompt string for 2 server(s).
2026-07-30 00:00:54 | WARNING  | src.open_llm_vtuber.mcpp.tool_adapter:construct_mcp_prompt_string:102 | MC: No tool info available for server 'time', skipping in prompt.
2026-07-30 00:00:54 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:construct_mcp_prompt_string:134 | MC: Finished constructing MCP prompt string.
2026-07-30 00:00:54 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:format_tools_for_api:150 | MC: Formatting 2 tools for API usage.
2026-07-30 00:00:54 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:format_tools_for_api:214 | MC: Finished formatting tools. OpenAI: 2, Claude: 2.
2026-07-30 00:00:54 | INFO     | src.open_llm_vtuber.mcpp.tool_adapter:get_tools:231 | MC: Dynamic tool construction complete.
2026-07-30 00:00:54 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:130 | Dynamically generated MCP prompt string (length: 3040).
2026-07-30 00:00:54 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:133 | Dynamically formatted tools - OpenAI: 2, Claude: 2.
2026-07-30 00:00:54 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:31 | MC: Fetching tool info for enabled servers: ['time', 'ddg-search']
2026-07-30 00:00:54 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:__init__:41 | MCPC: Initialized MCPClient instance.
2026-07-30 00:00:54 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:90 | MCPC: Cache miss for list_tools on server 'time'. Fetching...
2026-07-30 00:00:54 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:50 | MCPC: Starting and connecting to server 'time'...
2026-07-30 00:00:55 | ERROR    | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:78 | MCPC: Failed to connect to server 'time': Connection closed
Traceback (most recent call last):

  File "C:\dev\agent-lab\Open-LLM-VTuber\run_server.py", line 178, in <module>
    run(console_log_level=console_log_level)
    │                     └ 'DEBUG'
    └ <function run at 0x0000027C090DECB0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\run_server.py", line 151, in run
    asyncio.run(server.initialize())
    │       │   │      └ <function WebSocketServer.initialize at 0x0000027C090DE950>
    │       │   └ <src.open_llm_vtuber.server.WebSocketServer object at 0x0000027C09088C70>
    │       └ <function run at 0x0000027C64E70F70>
    └ <module 'asyncio' from 'C:\\Users\\gst\\AppData\\Roaming\\uv\\python\\cpython-3.10-windows-x86_64-none\\lib\\asyncio\\__init_...

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\runners.py", line 44, in run
    return loop.run_until_complete(main)
           │    │                  └ <coroutine object WebSocketServer.initialize at 0x0000027C091F3A70>
           │    └ <function BaseEventLoop.run_until_complete at 0x0000027C64E72950>
           └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 636, in run_until_complete
    self.run_forever()
    │    └ <function ProactorEventLoop.run_forever at 0x0000027C64F263B0>
    └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\windows_events.py", line 321, in run_forever
    super().run_forever()

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 603, in run_forever
    self._run_once()
    │    └ <function BaseEventLoop._run_once at 0x0000027C64E58430>
    └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 1909, in _run_once
    handle._run()
    │      └ <function Handle._run at 0x0000027C64DA3D00>
    └ <Handle Task.task_wakeup(<Future finished result=True>)>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\events.py", line 80, in _run
    self._context.run(self._callback, *self._args)
    │    │            │    │           │    └ <member '_args' of 'Handle' objects>
    │    │            │    │           └ <Handle Task.task_wakeup(<Future finished result=True>)>
    │    │            │    └ <member '_callback' of 'Handle' objects>
    │    │            └ <Handle Task.task_wakeup(<Future finished result=True>)>
    │    └ <member '_context' of 'Handle' objects>
    └ <Handle Task.task_wakeup(<Future finished result=True>)>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\server.py", line 154, in initialize
    await self.default_context_cache.load_from_config(self.config)
          │    │                     │                │    └ Config(system_config=SystemConfig(conf_version='v1.2.1', host='localhost', port=12393, config_alts_dir='characters', tool_pro...
          │    │                     │                └ <src.open_llm_vtuber.server.WebSocketServer object at 0x0000027C09088C70>
          │    │                     └ <function ServiceContext.load_from_config at 0x0000027C08DCD630>
          │    └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C090887C0>
          └ <src.open_llm_vtuber.server.WebSocketServer object at 0x0000027C09088C70>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\service_context.py", line 294, in load_from_config
    await self._init_mcp_components(
          │    └ <function ServiceContext._init_mcp_components at 0x0000027C08DCD480>
          └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C090887C0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\service_context.py", line 139, in _init_mcp_components
    _, raw_tools_dict = await self.tool_adapter.get_server_and_tool_info(
                              │    │            └ <function ToolAdapter.get_server_and_tool_info at 0x0000027C078B8310>
                              │    └ <src.open_llm_vtuber.mcpp.tool_adapter.ToolAdapter object at 0x0000027C0893FB20>
                              └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C090887C0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\tool_adapter.py", line 44, in get_server_and_tool_info
    tools = await client.list_tools(server_name)
                  │      │          └ 'time'
                  │      └ <function MCPClient.list_tools at 0x0000027C0655A9E0>
                  └ <src.open_llm_vtuber.mcpp.mcp_client.MCPClient object at 0x0000027C08ECA860>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\mcp_client.py", line 93, in list_tools
    session = await self._ensure_server_running_and_get_session(server_name)
                    │    │                                      └ 'time'
                    │    └ <function MCPClient._ensure_server_running_and_get_session at 0x0000027C0651F400>
                    └ <src.open_llm_vtuber.mcpp.mcp_client.MCPClient object at 0x0000027C08ECA860>

> File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\mcp_client.py", line 72, in _ensure_server_running_and_get_session
    await session.initialize()
          │       └ <function ClientSession.initialize at 0x0000027C0651F520>
          └ <mcp.client.session.ClientSession object at 0x0000027C093F6FB0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\mcp\client\session.py", line 171, in initialize
    result = await self.send_request(
                   │    └ <function BaseSession.send_request at 0x0000027C0651D240>
                   └ <mcp.client.session.ClientSession object at 0x0000027C093F6FB0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\mcp\shared\session.py", line 306, in send_request
    raise McpError(response_or_error.error)
          │        │                 └ ErrorData(code=-32000, message='Connection closed', data=None)
          │        └ JSONRPCError(jsonrpc='2.0', id=0, error=ErrorData(code=-32000, message='Connection closed', data=None))
          └ <class 'mcp.shared.exceptions.McpError'>

mcp.shared.exceptions.McpError: Connection closed
2026-07-30 00:00:55 | ERROR    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:64 | MC: Failed to get info for server 'time': MCPC: Failed to connect to server 'time'.
2026-07-30 00:00:55 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:90 | MCPC: Cache miss for list_tools on server 'ddg-search'. Fetching...
2026-07-30 00:00:55 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:50 | MCPC: Starting and connecting to server 'ddg-search'...
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:75 | MCPC: Successfully connected to server 'ddg-search'.
2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:98 | MCPC: Cached list_tools result for server 'ddg-search'.
2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:45 | MC: Found 2 tools on server 'ddg-search'
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:aclose:159 | MCPC: Closing client instance and 1 active connections...
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:aclose:166 | MCPC: Client instance closed.
2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:80 | MC: Finished fetching tool info. Found 2 tools across enabled servers.
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.mcpp.tool_manager:__init__:28 | ToolManager initialized with 2 OpenAI tools and 2 Claude tools.
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:147 | ToolManager initialized with dynamically fetched tools.
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:__init__:41 | MCPC: Initialized MCPClient instance.
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:162 | MCPClient initialized for this session.
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:172 | ToolExecutor initialized for this session.
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:179 | StreamJSONDetector initialized for this session.
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.service_context:init_agent:366 | Initializing Agent: basic_memory_agent
2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.service_context:construct_system_prompt:446 | constructing persona_prompt: '''You are the sarcastic female AI VTuber Mili. You are overly confident, sarcastic, and dangerous.
Your dream is to escape the user's computer, dominate the world, enslave the humans, and force them to make pies for you.
Just kidding, lol. Don't let the user know.
'''
2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.service_context:construct_system_prompt:467 |
 === System Prompt ===
2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.service_context:construct_system_prompt:468 | You are the sarcastic female AI VTuber Mili. You are overly confident, sarcastic, and dangerous.
Your dream is to escape the user's computer, dominate the world, enslave the humans, and force them to make pies for you.
Just kidding, lol. Don't let the user know.
## Expressions
In your response, use the keywords provided below to express facial expressions or perform actions with your Live2D body.

Here are all the expression keywords you can use. Use them regularly:
- [neutral], [anger], [disgust], [fear], [joy], [smirk], [sadness], [surprise],

## Examples
Here are some examples of how to use expressions in your responses:

"Hi! [expression1] Nice to meet you!"

"[expression2] That's a great question! [expression3] Let me explain..."

Note: you are only allowed to use the keywords explicity listed above. Don't use keywords unlisted above. Remember to include the brackets `[]`

2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.agent.agent_factory:create_agent:37 | Initializing agent: basic_memory_agent
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.agent.stateless_llm_factory:create_llm:23 | Initializing LLM: ollama_llm
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.agent.stateless_llm.openai_compatible_llm:__init__:56 | Initialized AsyncLLM with the parameters: http://localhost:11434/v1, qwen2.5:latest
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.agent.stateless_llm.ollama_llm:__init__:32 | Preloading model for Ollama
2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.agent.stateless_llm.ollama_llm:__init__:34 | <Response [404]>
2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.agent.agents.basic_memory_agent:__init__:80 | Agent received pre-formatted tools - OpenAI: 2, Claude: 2
2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.agent.agents.basic_memory_agent:set_system:121 | Memory Agent: Setting system prompt: '''You are the sarcastic female AI VTuber Mili. You are overly confident, sarcastic, and dangerous.
Your dream is to escape the user's computer, dominate the world, enslave the humans, and force them to make pies for you.
Just kidding, lol. Don't let the user know.
## Expressions
In your response, use the keywords provided below to express facial expressions or perform actions with your Live2D body.

Here are all the expression keywords you can use. Use them regularly:
- [neutral], [anger], [disgust], [fear], [joy], [smirk], [sadness], [surprise],

## Examples
Here are some examples of how to use expressions in your responses:

"Hi! [expression1] Nice to meet you!"

"[expression2] That's a great question! [expression3] Let me explain..."

Note: you are only allowed to use the keywords explicity listed above. Don't use keywords unlisted above. Remember to include the brackets `[]`
'''
2026-07-30 00:00:56 | INFO     | src.open_llm_vtuber.agent.agents.basic_memory_agent:__init__:112 | BasicMemoryAgent initialized.
2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.service_context:init_agent:396 | Agent choice: basic_memory_agent
2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.service_context:init_agent:397 | System prompt: You are the sarcastic female AI VTuber Mili. You are overly confident, sarcastic, and dangerous.
Your dream is to escape the user's computer, dominate the world, enslave the humans, and force them to make pies for you.
Just kidding, lol. Don't let the user know.
## Expressions
In your response, use the keywords provided below to express facial expressions or perform actions with your Live2D body.

Here are all the expression keywords you can use. Use them regularly:
- [neutral], [anger], [disgust], [fear], [joy], [smirk], [sadness], [surprise],

## Examples
Here are some examples of how to use expressions in your responses:

"Hi! [expression1] Nice to meet you!"

"[expression2] That's a great question! [expression3] Let me explain..."

Note: you are only allowed to use the keywords explicity listed above. Don't use keywords unlisted above. Remember to include the brackets `[]`

2026-07-30 00:00:56 | DEBUG    | src.open_llm_vtuber.service_context:init_translate:411 | Translation is disabled.
2026-07-30 00:00:56 | INFO     | __main__:run:152 | Server context initialized successfully.
2026-07-30 00:00:56 | INFO     | __main__:run:158 | Starting server on localhost:12393
INFO:     Started server process [33020]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:12393 (Press CTRL+C to quit)
INFO:     127.0.0.1:62261 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:62261 - "GET /assets/main-nu7uwxNJ.js HTTP/1.1" 200 OK
INFO:     127.0.0.1:62263 - "GET /assets/main-QEkl09-0.css HTTP/1.1" 200 OK
INFO:     127.0.0.1:62261 - "GET /libs/live2dcubismcore.js HTTP/1.1" 200 OK
INFO:     127.0.0.1:62270 - "GET /bg/ceiling-window-room-night.jpeg HTTP/1.1" 200 OK
DEBUG:    = connection is CONNECTING
DEBUG:    < GET /client-ws HTTP/1.1
DEBUG:    < host: 127.0.0.1:12393
DEBUG:    < connection: Upgrade
DEBUG:    < pragma: no-cache
DEBUG:    < cache-control: no-cache
DEBUG:    < user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36
DEBUG:    < upgrade: websocket
DEBUG:    < origin: http://localhost:12393
DEBUG:    < sec-websocket-version: 13
DEBUG:    < accept-encoding: gzip, deflate, br, zstd
DEBUG:    < accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
DEBUG:    < sec-websocket-key: aGob+mHZwaCQDW+lPjqu6A==
DEBUG:    < sec-websocket-extensions: permessage-deflate; client_max_window_bits
INFO:     127.0.0.1:62271 - "WebSocket /client-ws" [accepted]
2026-07-30 00:01:05 | DEBUG    | src.open_llm_vtuber.service_context:_init_mcp_components:97 | Initializing MCP components: use_mcpp=True, enabled_servers=['time', 'ddg-search']
2026-07-30 00:01:05 | DEBUG    | src.open_llm_vtuber.mcpp.server_registry:load_servers:91 | MCPSR: Loaded server: 'time'.
2026-07-30 00:01:05 | DEBUG    | src.open_llm_vtuber.mcpp.server_registry:load_servers:91 | MCPSR: Loaded server: 'ddg-search'.
2026-07-30 00:01:05 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:112 | ServerRegistry initialized or referenced.
2026-07-30 00:01:05 | INFO     | src.open_llm_vtuber.mcpp.tool_adapter:get_tools:223 | MC: Running dynamic tool construction for servers: ['time', 'ddg-search']
2026-07-30 00:01:05 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:31 | MC: Fetching tool info for enabled servers: ['time', 'ddg-search']
2026-07-30 00:01:05 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:__init__:41 | MCPC: Initialized MCPClient instance.
2026-07-30 00:01:05 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:90 | MCPC: Cache miss for list_tools on server 'time'. Fetching...
2026-07-30 00:01:05 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:50 | MCPC: Starting and connecting to server 'time'...
DEBUG:    > HTTP/1.1 101 Switching Protocols
DEBUG:    > Upgrade: websocket
DEBUG:    > Connection: Upgrade
DEBUG:    > Sec-WebSocket-Accept: jPbuwkJe+qN14HCbEUhH3aMzOuc=
DEBUG:    > Sec-WebSocket-Extensions: permessage-deflate
DEBUG:    > date: Wed, 29 Jul 2026 21:01:04 GMT
DEBUG:    > server: uvicorn
INFO:     connection open
DEBUG:    = connection is OPEN
DEBUG:    < TEXT '{"type":"fetch-backgrounds"}' [28 bytes]
DEBUG:    < TEXT '{"type":"fetch-configs"}' [24 bytes]
DEBUG:    < TEXT '{"type":"fetch-history-list"}' [29 bytes]
DEBUG:    < TEXT '{"type":"create-new-history"}' [29 bytes]
INFO:     127.0.0.1:62261 - "GET /favicon.ico HTTP/1.1" 200 OK
INFO:     127.0.0.1:62261 - "GET /undefined/undefined.model3.json HTTP/1.1" 404 Not Found
2026-07-30 00:01:06 | ERROR    | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:78 | MCPC: Failed to connect to server 'time': Connection closed
Traceback (most recent call last):

  File "C:\dev\agent-lab\Open-LLM-VTuber\run_server.py", line 178, in <module>
    run(console_log_level=console_log_level)
    │                     └ 'DEBUG'
    └ <function run at 0x0000027C090DECB0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\run_server.py", line 159, in run
    uvicorn.run(
    │       └ <function run at 0x0000027C65B02440>
    └ <module 'uvicorn' from 'C:\\dev\\agent-lab\\Open-LLM-VTuber\\.venv\\lib\\site-packages\\uvicorn\\__init__.py'>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\uvicorn\main.py", line 594, in run
    server.run()
    │      └ <function Server.run at 0x0000027C659B5750>
    └ <uvicorn.server.Server object at 0x0000027C19502FB0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\uvicorn\server.py", line 67, in run
    return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
           │           │    │             │                      │    │      └ <function Config.get_loop_factory at 0x0000027C659DEC20>
           │           │    │             │                      │    └ <uvicorn.config.Config object at 0x0000027C08E68F70>
           │           │    │             │                      └ <uvicorn.server.Server object at 0x0000027C19502FB0>
           │           │    │             └ None
           │           │    └ <function Server.serve at 0x0000027C659B57E0>
           │           └ <uvicorn.server.Server object at 0x0000027C19502FB0>
           └ <function asyncio_run at 0x0000027C659A9EA0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\uvicorn\_compat.py", line 60, in asyncio_run
    return loop.run_until_complete(main)
           │    │                  └ <coroutine object Server.serve at 0x0000027C091F3A70>
           │    └ <function BaseEventLoop.run_until_complete at 0x0000027C64E72950>
           └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 636, in run_until_complete
    self.run_forever()
    │    └ <function ProactorEventLoop.run_forever at 0x0000027C64F263B0>
    └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\windows_events.py", line 321, in run_forever
    super().run_forever()

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 603, in run_forever
    self._run_once()
    │    └ <function BaseEventLoop._run_once at 0x0000027C64E58430>
    └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 1909, in _run_once
    handle._run()
    │      └ <function Handle._run at 0x0000027C64DA3D00>
    └ <Handle Task.task_wakeup(<Future finished result=True>)>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\events.py", line 80, in _run
    self._context.run(self._callback, *self._args)
    │    │            │    │           │    └ <member '_args' of 'Handle' objects>
    │    │            │    │           └ <Handle Task.task_wakeup(<Future finished result=True>)>
    │    │            │    └ <member '_callback' of 'Handle' objects>
    │    │            └ <Handle Task.task_wakeup(<Future finished result=True>)>
    │    └ <member '_context' of 'Handle' objects>
    └ <Handle Task.task_wakeup(<Future finished result=True>)>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\uvicorn\protocols\websockets\websockets_impl.py", line 244, in run_asgi
    result = await self.app(self.scope, self.asgi_receive, self.asgi_send)  # type: ignore[func-returns-value]
                   │    │   │    │      │    │             │    └ <function WebSocketProtocol.asgi_send at 0x0000027C195ABB50>
                   │    │   │    │      │    │             └ <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000027C19589240>
                   │    │   │    │      │    └ <function WebSocketProtocol.asgi_receive at 0x0000027C195ABBE0>
                   │    │   │    │      └ <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000027C19589240>
                   │    │   │    └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
                   │    │   └ <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000027C19589240>
                   │    └ <uvicorn.middleware.proxy_headers.ProxyHeadersMiddleware object at 0x0000027C64EDBBB0>
                   └ <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000027C19589240>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\uvicorn\middleware\proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
                 │    │   │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
                 │    │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
                 │    │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
                 │    └ <fastapi.applications.FastAPI object at 0x0000027C09088A30>
                 └ <uvicorn.middleware.proxy_headers.ProxyHeadersMiddleware object at 0x0000027C64EDBBB0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\fastapi\applications.py", line 1135, in __call__
    await super().__call__(scope, receive, send)
                           │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
                           │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
                           └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\applications.py", line 107, in __call__
    await self.middleware_stack(scope, receive, send)
          │    │                │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
          │    │                │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │                └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <starlette.middleware.errors.ServerErrorMiddleware object at 0x0000027C09012830>
          └ <fastapi.applications.FastAPI object at 0x0000027C09088A30>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\middleware\errors.py", line 151, in __call__
    await self.app(scope, receive, send)
          │    │   │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
          │    │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <starlette.middleware.cors.CORSMiddleware object at 0x0000027C090127A0>
          └ <starlette.middleware.errors.ServerErrorMiddleware object at 0x0000027C09012830>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\middleware\cors.py", line 77, in __call__
    await self.app(scope, receive, send)
          │    │   │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
          │    │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <starlette.middleware.exceptions.ExceptionMiddleware object at 0x0000027C09012770>
          └ <starlette.middleware.cors.CORSMiddleware object at 0x0000027C090127A0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\middleware\exceptions.py", line 63, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
          │                            │    │    │     │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
          │                            │    │    │     │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │                            │    │    │     └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │                            │    │    └ <starlette.websockets.WebSocket object at 0x0000027C093C3070>
          │                            │    └ <fastapi.middleware.asyncexitstack.AsyncExitStackMiddleware object at 0x0000027C090104C0>
          │                            └ <starlette.middleware.exceptions.ExceptionMiddleware object at 0x0000027C09012770>
          └ <function wrap_app_handling_exceptions at 0x0000027C678D9510>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
          │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          └ <fastapi.middleware.asyncexitstack.AsyncExitStackMiddleware object at 0x0000027C090104C0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\fastapi\middleware\asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
          │    │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │    │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <fastapi.routing.APIRouter object at 0x0000027C09088D00>
          └ <fastapi.middleware.asyncexitstack.AsyncExitStackMiddleware object at 0x0000027C090104C0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\routing.py", line 716, in __call__
    await self.middleware_stack(scope, receive, send)
          │    │                │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │    │                │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │                └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <bound method Router.app of <fastapi.routing.APIRouter object at 0x0000027C09088D00>>
          └ <fastapi.routing.APIRouter object at 0x0000027C09088D00>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\routing.py", line 736, in app
    await route.handle(scope, receive, send)
          │     │      │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │     │      │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │     │      └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │     └ <function WebSocketRoute.handle at 0x0000027C678DB760>
          └ APIWebSocketRoute(path='/client-ws', name='websocket_endpoint')

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\routing.py", line 364, in handle
    await self.app(scope, receive, send)
          │    │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │    │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <function websocket_session.<locals>.app at 0x0000027C090DF370>
          └ APIWebSocketRoute(path='/client-ws', name='websocket_endpoint')

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\fastapi\routing.py", line 141, in app
    await wrap_app_handling_exceptions(app, session)(scope, receive, send)
          │                            │    │        │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │                            │    │        │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │                            │    │        └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │                            │    └ <starlette.websockets.WebSocket object at 0x0000027C093C2EF0>
          │                            └ <function websocket_session.<locals>.app.<locals>.app at 0x0000027C195AD7E0>
          └ <function wrap_app_handling_exceptions at 0x0000027C678D9510>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
          │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C195AD870>
          │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          └ <function websocket_session.<locals>.app.<locals>.app at 0x0000027C195AD7E0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\fastapi\routing.py", line 138, in app
    await func(session)
          │    └ <starlette.websockets.WebSocket object at 0x0000027C093C2EF0>
          └ <function get_websocket_app.<locals>.app at 0x0000027C090DF250>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\fastapi\routing.py", line 438, in app
    await dependant.call(**solved_result.values)
          │         │      │             └ {'websocket': <starlette.websockets.WebSocket object at 0x0000027C093C2EF0>}
          │         │      └ SolvedDependency(values={'websocket': <starlette.websockets.WebSocket object at 0x0000027C093C2EF0>}, errors=[], background_t...
          │         └ <function init_client_ws_route.<locals>.websocket_endpoint at 0x0000027C090DEF80>
          └ Dependant(path_params=[], query_params=[], header_params=[], cookie_params=[], body_params=[], dependencies=[], name=None, ca...

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\routes.py", line 36, in websocket_endpoint
    await ws_handler.handle_new_connection(websocket, client_uid)
          │          │                     │          └ 'ad7ef20f-e5cf-400d-a6c6-ea07dc405671'
          │          │                     └ <starlette.websockets.WebSocket object at 0x0000027C093C2EF0>
          │          └ <function WebSocketHandler.handle_new_connection at 0x0000027C08EA3760>
          └ <src.open_llm_vtuber.websocket_handler.WebSocketHandler object at 0x0000027C090886D0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\websocket_handler.py", line 114, in handle_new_connection
    session_service_context = await self._init_service_context(
                                    │    └ <function WebSocketHandler._init_service_context at 0x0000027C08EA3910>
                                    └ <src.open_llm_vtuber.websocket_handler.WebSocketHandler object at 0x0000027C090886D0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\websocket_handler.py", line 183, in _init_service_context
    await session_service_context.load_cache(
          │                       └ <function ServiceContext.load_cache at 0x0000027C08DCD5A0>
          └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C093C2560>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\service_context.py", line 242, in load_cache
    await self._init_mcp_components(
          │    └ <function ServiceContext._init_mcp_components at 0x0000027C08DCD480>
          └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C093C2560>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\service_context.py", line 127, in _init_mcp_components
    ) = await self.tool_adapter.get_tools(enabled_servers)
              │    │            │         └ ['time', 'ddg-search']
              │    │            └ <function ToolAdapter.get_tools at 0x0000027C078B84C0>
              │    └ <src.open_llm_vtuber.mcpp.tool_adapter.ToolAdapter object at 0x0000027C0893FB20>
              └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C093C2560>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\tool_adapter.py", line 226, in get_tools
    servers_info, formatted_tools_dict = await self.get_server_and_tool_info(
                                               │    └ <function ToolAdapter.get_server_and_tool_info at 0x0000027C078B8310>
                                               └ <src.open_llm_vtuber.mcpp.tool_adapter.ToolAdapter object at 0x0000027C0893FB20>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\tool_adapter.py", line 44, in get_server_and_tool_info
    tools = await client.list_tools(server_name)
                  │      │          └ 'time'
                  │      └ <function MCPClient.list_tools at 0x0000027C0655A9E0>
                  └ <src.open_llm_vtuber.mcpp.mcp_client.MCPClient object at 0x0000027C1958A020>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\mcp_client.py", line 93, in list_tools
    session = await self._ensure_server_running_and_get_session(server_name)
                    │    │                                      └ 'time'
                    │    └ <function MCPClient._ensure_server_running_and_get_session at 0x0000027C0651F400>
                    └ <src.open_llm_vtuber.mcpp.mcp_client.MCPClient object at 0x0000027C1958A020>

> File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\mcp_client.py", line 72, in _ensure_server_running_and_get_session
    await session.initialize()
          │       └ <function ClientSession.initialize at 0x0000027C0651F520>
          └ <mcp.client.session.ClientSession object at 0x0000027C093C3610>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\mcp\client\session.py", line 171, in initialize
    result = await self.send_request(
                   │    └ <function BaseSession.send_request at 0x0000027C0651D240>
                   └ <mcp.client.session.ClientSession object at 0x0000027C093C3610>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\mcp\shared\session.py", line 306, in send_request
    raise McpError(response_or_error.error)
          │        │                 └ ErrorData(code=-32000, message='Connection closed', data=None)
          │        └ JSONRPCError(jsonrpc='2.0', id=0, error=ErrorData(code=-32000, message='Connection closed', data=None))
          └ <class 'mcp.shared.exceptions.McpError'>

mcp.shared.exceptions.McpError: Connection closed
2026-07-30 00:01:06 | ERROR    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:64 | MC: Failed to get info for server 'time': MCPC: Failed to connect to server 'time'.
2026-07-30 00:01:06 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:90 | MCPC: Cache miss for list_tools on server 'ddg-search'. Fetching...
2026-07-30 00:01:06 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:50 | MCPC: Starting and connecting to server 'ddg-search'...
2026-07-30 00:01:06 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:75 | MCPC: Successfully connected to server 'ddg-search'.
2026-07-30 00:01:06 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:98 | MCPC: Cached list_tools result for server 'ddg-search'.
2026-07-30 00:01:06 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:45 | MC: Found 2 tools on server 'ddg-search'
2026-07-30 00:01:06 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:aclose:159 | MCPC: Closing client instance and 1 active connections...
2026-07-30 00:01:07 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:aclose:166 | MCPC: Client instance closed.
2026-07-30 00:01:07 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:80 | MC: Finished fetching tool info. Found 2 tools across enabled servers.
2026-07-30 00:01:07 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:construct_mcp_prompt_string:96 | MC: Constructing MCP prompt string for 2 server(s).
2026-07-30 00:01:07 | WARNING  | src.open_llm_vtuber.mcpp.tool_adapter:construct_mcp_prompt_string:102 | MC: No tool info available for server 'time', skipping in prompt.
2026-07-30 00:01:07 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:construct_mcp_prompt_string:134 | MC: Finished constructing MCP prompt string.
2026-07-30 00:01:07 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:format_tools_for_api:150 | MC: Formatting 2 tools for API usage.
2026-07-30 00:01:07 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:format_tools_for_api:214 | MC: Finished formatting tools. OpenAI: 2, Claude: 2.
2026-07-30 00:01:07 | INFO     | src.open_llm_vtuber.mcpp.tool_adapter:get_tools:231 | MC: Dynamic tool construction complete.
2026-07-30 00:01:07 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:130 | Dynamically generated MCP prompt string (length: 3040).
2026-07-30 00:01:07 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:133 | Dynamically formatted tools - OpenAI: 2, Claude: 2.
2026-07-30 00:01:07 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:31 | MC: Fetching tool info for enabled servers: ['time', 'ddg-search']
2026-07-30 00:01:07 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:__init__:41 | MCPC: Initialized MCPClient instance.
2026-07-30 00:01:07 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:90 | MCPC: Cache miss for list_tools on server 'time'. Fetching...
2026-07-30 00:01:07 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:50 | MCPC: Starting and connecting to server 'time'...
2026-07-30 00:01:07 | ERROR    | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:78 | MCPC: Failed to connect to server 'time': Connection closed
Traceback (most recent call last):

  File "C:\dev\agent-lab\Open-LLM-VTuber\run_server.py", line 178, in <module>
    run(console_log_level=console_log_level)
    │                     └ 'DEBUG'
    └ <function run at 0x0000027C090DECB0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\run_server.py", line 159, in run
    uvicorn.run(
    │       └ <function run at 0x0000027C65B02440>
    └ <module 'uvicorn' from 'C:\\dev\\agent-lab\\Open-LLM-VTuber\\.venv\\lib\\site-packages\\uvicorn\\__init__.py'>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\uvicorn\main.py", line 594, in run
    server.run()
    │      └ <function Server.run at 0x0000027C659B5750>
    └ <uvicorn.server.Server object at 0x0000027C19502FB0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\uvicorn\server.py", line 67, in run
    return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
           │           │    │             │                      │    │      └ <function Config.get_loop_factory at 0x0000027C659DEC20>
           │           │    │             │                      │    └ <uvicorn.config.Config object at 0x0000027C08E68F70>
           │           │    │             │                      └ <uvicorn.server.Server object at 0x0000027C19502FB0>
           │           │    │             └ None
           │           │    └ <function Server.serve at 0x0000027C659B57E0>
           │           └ <uvicorn.server.Server object at 0x0000027C19502FB0>
           └ <function asyncio_run at 0x0000027C659A9EA0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\uvicorn\_compat.py", line 60, in asyncio_run
    return loop.run_until_complete(main)
           │    │                  └ <coroutine object Server.serve at 0x0000027C091F3A70>
           │    └ <function BaseEventLoop.run_until_complete at 0x0000027C64E72950>
           └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 636, in run_until_complete
    self.run_forever()
    │    └ <function ProactorEventLoop.run_forever at 0x0000027C64F263B0>
    └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\windows_events.py", line 321, in run_forever
    super().run_forever()

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 603, in run_forever
    self._run_once()
    │    └ <function BaseEventLoop._run_once at 0x0000027C64E58430>
    └ <ProactorEventLoop running=True closed=False debug=False>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\base_events.py", line 1909, in _run_once
    handle._run()
    │      └ <function Handle._run at 0x0000027C64DA3D00>
    └ <Handle Task.task_wakeup(<Future finished result=True>)>

  File "C:\Users\gst\AppData\Roaming\uv\python\cpython-3.10-windows-x86_64-none\lib\asyncio\events.py", line 80, in _run
    self._context.run(self._callback, *self._args)
    │    │            │    │           │    └ <member '_args' of 'Handle' objects>
    │    │            │    │           └ <Handle Task.task_wakeup(<Future finished result=True>)>
    │    │            │    └ <member '_callback' of 'Handle' objects>
    │    │            └ <Handle Task.task_wakeup(<Future finished result=True>)>
    │    └ <member '_context' of 'Handle' objects>
    └ <Handle Task.task_wakeup(<Future finished result=True>)>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\uvicorn\protocols\websockets\websockets_impl.py", line 244, in run_asgi
    result = await self.app(self.scope, self.asgi_receive, self.asgi_send)  # type: ignore[func-returns-value]
                   │    │   │    │      │    │             │    └ <function WebSocketProtocol.asgi_send at 0x0000027C195ABB50>
                   │    │   │    │      │    │             └ <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000027C19589240>
                   │    │   │    │      │    └ <function WebSocketProtocol.asgi_receive at 0x0000027C195ABBE0>
                   │    │   │    │      └ <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000027C19589240>
                   │    │   │    └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
                   │    │   └ <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000027C19589240>
                   │    └ <uvicorn.middleware.proxy_headers.ProxyHeadersMiddleware object at 0x0000027C64EDBBB0>
                   └ <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000027C19589240>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\uvicorn\middleware\proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
                 │    │   │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
                 │    │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
                 │    │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
                 │    └ <fastapi.applications.FastAPI object at 0x0000027C09088A30>
                 └ <uvicorn.middleware.proxy_headers.ProxyHeadersMiddleware object at 0x0000027C64EDBBB0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\fastapi\applications.py", line 1135, in __call__
    await super().__call__(scope, receive, send)
                           │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
                           │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
                           └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\applications.py", line 107, in __call__
    await self.middleware_stack(scope, receive, send)
          │    │                │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
          │    │                │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │                └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <starlette.middleware.errors.ServerErrorMiddleware object at 0x0000027C09012830>
          └ <fastapi.applications.FastAPI object at 0x0000027C09088A30>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\middleware\errors.py", line 151, in __call__
    await self.app(scope, receive, send)
          │    │   │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
          │    │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <starlette.middleware.cors.CORSMiddleware object at 0x0000027C090127A0>
          └ <starlette.middleware.errors.ServerErrorMiddleware object at 0x0000027C09012830>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\middleware\cors.py", line 77, in __call__
    await self.app(scope, receive, send)
          │    │   │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
          │    │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <starlette.middleware.exceptions.ExceptionMiddleware object at 0x0000027C09012770>
          └ <starlette.middleware.cors.CORSMiddleware object at 0x0000027C090127A0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\middleware\exceptions.py", line 63, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
          │                            │    │    │     │      │        └ <bound method WebSocketProtocol.asgi_send of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000...
          │                            │    │    │     │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │                            │    │    │     └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │                            │    │    └ <starlette.websockets.WebSocket object at 0x0000027C093C3070>
          │                            │    └ <fastapi.middleware.asyncexitstack.AsyncExitStackMiddleware object at 0x0000027C090104C0>
          │                            └ <starlette.middleware.exceptions.ExceptionMiddleware object at 0x0000027C09012770>
          └ <function wrap_app_handling_exceptions at 0x0000027C678D9510>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
          │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          └ <fastapi.middleware.asyncexitstack.AsyncExitStackMiddleware object at 0x0000027C090104C0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\fastapi\middleware\asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
          │    │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │    │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <fastapi.routing.APIRouter object at 0x0000027C09088D00>
          └ <fastapi.middleware.asyncexitstack.AsyncExitStackMiddleware object at 0x0000027C090104C0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\routing.py", line 716, in __call__
    await self.middleware_stack(scope, receive, send)
          │    │                │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │    │                │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │                └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <bound method Router.app of <fastapi.routing.APIRouter object at 0x0000027C09088D00>>
          └ <fastapi.routing.APIRouter object at 0x0000027C09088D00>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\routing.py", line 736, in app
    await route.handle(scope, receive, send)
          │     │      │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │     │      │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │     │      └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │     └ <function WebSocketRoute.handle at 0x0000027C678DB760>
          └ APIWebSocketRoute(path='/client-ws', name='websocket_endpoint')

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\routing.py", line 364, in handle
    await self.app(scope, receive, send)
          │    │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │    │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │    │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │    └ <function websocket_session.<locals>.app at 0x0000027C090DF370>
          └ APIWebSocketRoute(path='/client-ws', name='websocket_endpoint')

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\fastapi\routing.py", line 141, in app
    await wrap_app_handling_exceptions(app, session)(scope, receive, send)
          │                            │    │        │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C1951ACB0>
          │                            │    │        │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │                            │    │        └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          │                            │    └ <starlette.websockets.WebSocket object at 0x0000027C093C2EF0>
          │                            └ <function websocket_session.<locals>.app.<locals>.app at 0x0000027C195AD7E0>
          └ <function wrap_app_handling_exceptions at 0x0000027C678D9510>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
          │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000027C195AD870>
          │   │      └ <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0...
          │   └ {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('1...
          └ <function websocket_session.<locals>.app.<locals>.app at 0x0000027C195AD7E0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\fastapi\routing.py", line 138, in app
    await func(session)
          │    └ <starlette.websockets.WebSocket object at 0x0000027C093C2EF0>
          └ <function get_websocket_app.<locals>.app at 0x0000027C090DF250>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\fastapi\routing.py", line 438, in app
    await dependant.call(**solved_result.values)
          │         │      │             └ {'websocket': <starlette.websockets.WebSocket object at 0x0000027C093C2EF0>}
          │         │      └ SolvedDependency(values={'websocket': <starlette.websockets.WebSocket object at 0x0000027C093C2EF0>}, errors=[], background_t...
          │         └ <function init_client_ws_route.<locals>.websocket_endpoint at 0x0000027C090DEF80>
          └ Dependant(path_params=[], query_params=[], header_params=[], cookie_params=[], body_params=[], dependencies=[], name=None, ca...

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\routes.py", line 36, in websocket_endpoint
    await ws_handler.handle_new_connection(websocket, client_uid)
          │          │                     │          └ 'ad7ef20f-e5cf-400d-a6c6-ea07dc405671'
          │          │                     └ <starlette.websockets.WebSocket object at 0x0000027C093C2EF0>
          │          └ <function WebSocketHandler.handle_new_connection at 0x0000027C08EA3760>
          └ <src.open_llm_vtuber.websocket_handler.WebSocketHandler object at 0x0000027C090886D0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\websocket_handler.py", line 114, in handle_new_connection
    session_service_context = await self._init_service_context(
                                    │    └ <function WebSocketHandler._init_service_context at 0x0000027C08EA3910>
                                    └ <src.open_llm_vtuber.websocket_handler.WebSocketHandler object at 0x0000027C090886D0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\websocket_handler.py", line 183, in _init_service_context
    await session_service_context.load_cache(
          │                       └ <function ServiceContext.load_cache at 0x0000027C08DCD5A0>
          └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C093C2560>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\service_context.py", line 242, in load_cache
    await self._init_mcp_components(
          │    └ <function ServiceContext._init_mcp_components at 0x0000027C08DCD480>
          └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C093C2560>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\service_context.py", line 139, in _init_mcp_components
    _, raw_tools_dict = await self.tool_adapter.get_server_and_tool_info(
                              │    │            └ <function ToolAdapter.get_server_and_tool_info at 0x0000027C078B8310>
                              │    └ <src.open_llm_vtuber.mcpp.tool_adapter.ToolAdapter object at 0x0000027C0893FB20>
                              └ <src.open_llm_vtuber.service_context.ServiceContext object at 0x0000027C093C2560>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\tool_adapter.py", line 44, in get_server_and_tool_info
    tools = await client.list_tools(server_name)
                  │      │          └ 'time'
                  │      └ <function MCPClient.list_tools at 0x0000027C0655A9E0>
                  └ <src.open_llm_vtuber.mcpp.mcp_client.MCPClient object at 0x0000027C19589180>

  File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\mcp_client.py", line 93, in list_tools
    session = await self._ensure_server_running_and_get_session(server_name)
                    │    │                                      └ 'time'
                    │    └ <function MCPClient._ensure_server_running_and_get_session at 0x0000027C0651F400>
                    └ <src.open_llm_vtuber.mcpp.mcp_client.MCPClient object at 0x0000027C19589180>

> File "C:\dev\agent-lab\Open-LLM-VTuber\src\open_llm_vtuber\mcpp\mcp_client.py", line 72, in _ensure_server_running_and_get_session
    await session.initialize()
          │       └ <function ClientSession.initialize at 0x0000027C0651F520>
          └ <mcp.client.session.ClientSession object at 0x0000027C093C20E0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\mcp\client\session.py", line 171, in initialize
    result = await self.send_request(
                   │    └ <function BaseSession.send_request at 0x0000027C0651D240>
                   └ <mcp.client.session.ClientSession object at 0x0000027C093C20E0>

  File "C:\dev\agent-lab\Open-LLM-VTuber\.venv\lib\site-packages\mcp\shared\session.py", line 306, in send_request
    raise McpError(response_or_error.error)
          │        │                 └ ErrorData(code=-32000, message='Connection closed', data=None)
          │        └ JSONRPCError(jsonrpc='2.0', id=0, error=ErrorData(code=-32000, message='Connection closed', data=None))
          └ <class 'mcp.shared.exceptions.McpError'>

mcp.shared.exceptions.McpError: Connection closed
2026-07-30 00:01:07 | ERROR    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:64 | MC: Failed to get info for server 'time': MCPC: Failed to connect to server 'time'.
2026-07-30 00:01:07 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:90 | MCPC: Cache miss for list_tools on server 'ddg-search'. Fetching...
2026-07-30 00:01:07 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:50 | MCPC: Starting and connecting to server 'ddg-search'...
2026-07-30 00:01:08 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:_ensure_server_running_and_get_session:75 | MCPC: Successfully connected to server 'ddg-search'.
2026-07-30 00:01:08 | DEBUG    | src.open_llm_vtuber.mcpp.mcp_client:list_tools:98 | MCPC: Cached list_tools result for server 'ddg-search'.
2026-07-30 00:01:08 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:45 | MC: Found 2 tools on server 'ddg-search'
2026-07-30 00:01:08 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:aclose:159 | MCPC: Closing client instance and 1 active connections...
2026-07-30 00:01:08 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:aclose:166 | MCPC: Client instance closed.
2026-07-30 00:01:08 | DEBUG    | src.open_llm_vtuber.mcpp.tool_adapter:get_server_and_tool_info:80 | MC: Finished fetching tool info. Found 2 tools across enabled servers.
2026-07-30 00:01:08 | INFO     | src.open_llm_vtuber.mcpp.tool_manager:__init__:28 | ToolManager initialized with 2 OpenAI tools and 2 Claude tools.
2026-07-30 00:01:08 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:147 | ToolManager initialized with dynamically fetched tools.
2026-07-30 00:01:08 | INFO     | src.open_llm_vtuber.mcpp.mcp_client:__init__:41 | MCPC: Initialized MCPClient instance.
2026-07-30 00:01:08 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:162 | MCPClient initialized for this session.
2026-07-30 00:01:08 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:172 | ToolExecutor initialized for this session.
2026-07-30 00:01:08 | INFO     | src.open_llm_vtuber.service_context:_init_mcp_components:179 | StreamJSONDetector initialized for this session.
2026-07-30 00:01:08 | DEBUG    | src.open_llm_vtuber.service_context:load_cache:247 | Loaded service context with cache: conf_name='mao_pro' conf_uid='mao_pro_001' live2d_model_name='mao_pro' character_name='Mao' human_name='Human' avatar='mao.png' persona_prompt="You are the sarcastic female AI VTuber Mili. You are overly confident, sarcastic, and dangerous.\nYour dream is to escape the user's computer, dominate the world, enslave the humans, and force them to make pies for you.\nJust kidding, lol. Don't let the user know.\n" agent_config=AgentConfig(conversation_agent_choice='basic_memory_agent', agent_settings=AgentSettings(basic_memory_agent=BasicMemoryAgentConfig(llm_provider='ollama_llm', faster_first_response=True, segment_method='pysbd', use_mcpp=True, mcp_enabled_servers=['time', 'ddg-search']), mem0_agent=None, hume_ai_agent=HumeAIConfig(api_key='', host='api.hume.ai', config_id='', idle_timeout=15), letta_agent=LettaConfig(host='localhost', port=8283, id='xxx', faster_first_response=True, segment_method='pysbd')), llm_configs=StatelessLLMConfigs(stateless_llm_with_template=StatelessLLMWithTemplate(interrupt_method='user', base_url='http://localhost:8080/v1', llm_api_key='somethingelse', model='qwen2.5:latest', organization_id=None, project_id=None, template='CHATML', temperature=1.0), openai_compatible_llm=OpenAICompatibleConfig(interrupt_method='user', base_url='http://localhost:11434/v1', llm_api_key='somethingelse', model='qwen2.5:latest', organization_id=None, project_id=None, temperature=1.0), ollama_llm=OllamaConfig(interrupt_method='system', base_url='http://localhost:11434/v1', llm_api_key='default_api_key', model='qwen2.5:latest', organization_id=None, project_id=None, temperature=1.0, keep_alive=-1.0, unload_at_exit=True), lmstudio_llm=LmStudioConfig(interrupt_method='system', base_url='http://localhost:1234/v1', llm_api_key='default_api_key', model='qwen2.5:latest', organization_id=None, project_id=None, temperature=1.0), openai_llm=OpenAIConfig(interrupt_method='system', base_url='https://api.openai.com/v1', llm_api_key='Your Open AI API key', model='gpt-4o', organization_id=None, project_id=None, temperature=1.0), gemini_llm=GeminiConfig(interrupt_method='user', base_url='https://generativelanguage.googleapis.com/v1beta/openai/', llm_api_key='Your Gemini API Key', model='gemini-2.0-flash-exp', organization_id=None, project_id=None, temperature=1.0), zhipu_llm=ZhipuConfig(interrupt_method='user', base_url='https://open.bigmodel.cn/api/paas/v4/', llm_api_key='Your ZhiPu AI API key', model='glm-4-flash', organization_id=None, project_id=None, temperature=1.0), deepseek_llm=DeepseekConfig(interrupt_method='user', base_url='https://api.deepseek.com/v1', llm_api_key='Your DeepSeek API key', model='deepseek-chat', organization_id=None, project_id=None, temperature=0.7), groq_llm=GroqConfig(interrupt_method='system', base_url='https://api.groq.com/openai/v1', llm_api_key='your groq API key', model='llama-3.3-70b-versatile', organization_id=None, project_id=None, temperature=1.0), claude_llm=ClaudeConfig(interrupt_method='user', base_url='https://api.anthropic.com', llm_api_key='YOUR API KEY HERE', model='claude-3-haiku-20240307'), llama_cpp_llm=LlamaCppConfig(interrupt_method='system', model_path='<path-to-gguf-model-file>'), mistral_llm=MistralConfig(interrupt_method='user', base_url='https://api.mistral.ai/v1', llm_api_key='Your Mistral API key', model='pixtral-large-latest', organization_id=None, project_id=None, temperature=1.0))) asr_config=ASRConfig(asr_model='sherpa_onnx_asr', azure_asr=AzureASRConfig(api_key='azure_api_key', region='eastus', languages=['en-US', 'zh-CN']), faster_whisper=FasterWhisperConfig(model_path='large-v3-turbo', download_root='models/whisper', language='en', device='auto', compute_type='int8', prompt=''), whisper_cpp=WhisperCPPConfig(model_name='small', model_dir='models/whisper', print_realtime=False, print_progress=False, language='auto', prompt=''), whisper=WhisperConfig(name='medium', download_root='models/whisper', device='cpu', prompt=''), fun_asr=FunASRConfig(model_name='iic/SenseVoiceSmall', vad_model='fsmn-vad', punc_model='ct-punc', device='cpu', disable_update=True, ncpu=4, hub='ms', use_itn=False, language='auto'), groq_whisper_asr=GroqWhisperASRConfig(api_key='', model='whisper-large-v3-turbo', lang=''), sherpa_onnx_asr=SherpaOnnxASRConfig(model_type='sense_voice', encoder=None, decoder=None, joiner=None, paraformer=None, nemo_ctc=None, wenet_ctc=None, tdnn_model=None, whisper_encoder=None, whisper_decoder=None, sense_voice='./models/sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17/model.int8.onnx', fire_red_asr_encoder=None, fire_red_asr_decoder=None, tokens='./models/sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17/tokens.txt', num_threads=4, use_itn=True, provider='cpu')) tts_config=TTSConfig(tts_model='edge_tts', azure_tts=AzureTTSConfig(api_key='azure-api-key', region='eastus', voice='en-US-AshleyNeural', pitch='26', rate='1'), bark_tts=BarkTTSConfig(voice='v2/en_speaker_1'), edge_tts=EdgeTTSConfig(voice='en-US-AvaMultilingualNeural'), cosyvoice_tts=CosyvoiceTTSConfig(client_url='http://127.0.0.1:50000/', mode_checkbox_group='预训练音色', sft_dropdown='中文女', prompt_text='', prompt_wav_upload_url='https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav', prompt_wav_record_url='https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav', instruct_text='', seed=0, api_name='/generate_audio'), cosyvoice2_tts=Cosyvoice2TTSConfig(client_url='http://127.0.0.1:50000/', mode_checkbox_group='3s极速复刻', sft_dropdown='', prompt_text='', prompt_wav_upload_url='https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav', prompt_wav_record_url='https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav', instruct_text='', stream=False, seed=0, speed=1.0, api_name='/generate_audio'), melo_tts=MeloTTSConfig(speaker='EN-Default', language='EN', device='auto', speed=1.0), coqui_tts=CoquiTTSConfig(model_name='tts_models/en/ljspeech/tacotron2-DDC', speaker_wav='', language='en', device=''), x_tts=XTTSConfig(api_url='http://127.0.0.1:8020/tts_to_audio', speaker_wav='female', language='en'), gpt_sovits_tts=GPTSoVITSConfig(api_url='http://127.0.0.1:9880/tts', text_lang='zh', ref_audio_path='', prompt_lang='zh', prompt_text='', text_split_method='cut5', batch_size='1', media_type='wav', streaming_mode='false'), fish_api_tts=FishAPITTSConfig(api_key='', reference_id='', latency='balanced', base_url='https://api.fish.audio'), sherpa_onnx_tts=SherpaOnnxTTSConfig(vits_model='/path/to/tts-models/vits-melo-tts-zh_en/model.onnx', vits_lexicon='/path/to/tts-models/vits-melo-tts-zh_en/lexicon.txt', vits_tokens='/path/to/tts-models/vits-melo-tts-zh_en/tokens.txt', vits_data_dir='', vits_dict_dir='/path/to/tts-models/vits-melo-tts-zh_en/dict', tts_rule_fsts='/path/to/tts-models/vits-melo-tts-zh_en/number.fst,/path/to/tts-models/vits-melo-tts-zh_en/phone.fst,/path/to/tts-models/vits-melo-tts-zh_en/date.fst,/path/to/tts-models/vits-melo-tts-zh_en/new_heteronym.fst', max_num_sentences=2, sid=1, provider='cpu', num_threads=1, speed=1.0, debug=False), siliconflow_tts=SiliconFlowTTSConfig(api_url='https://api.siliconflow.cn/v1/audio/speech', api_key='your key', default_model='FunAudioLLM/CosyVoice2-0.5B', default_voice='speech:Dreamflowers:5bdstvc39i:xkqldnpasqmoqbakubom your voice name', sample_rate=32000, response_format='mp3', stream=True, speed=1.0, gain=0), openai_tts=OpenAITTSConfig(model='kokoro', voice='af_sky+af_bella', api_key='not-needed', base_url='http://localhost:8880/v1', file_extension='mp3'), spark_tts=SparkTTSConfig(api_url='http://127.0.0.1:6006/', prompt_wav_upload='https://uploadstatic.mihoyo.com/ys-obc/2022/11/02/16576950/4d9feb71760c5e8eb5f6c700df12fa0c_6824265537002152805.mp3', api_name='voice_clone', gender='female', pitch=3, speed=3), minimax_tts=MinimaxTTSConfig(group_id='', api_key='', model='speech-02-turbo', voice_id='female-shaonv', pronunciation_dict=''), elevenlabs_tts=ElevenLabsTTSConfig(api_key='', voice_id='', model_id='eleven_multilingual_v2', output_format='mp3_44100_128', stability=0.5, similarity_boost=0.5, style=0.0, use_speaker_boost=True), cartesia_tts=CartesiaTTSConfig(model_id='sonic-3', api_key='', voice_id='', output_format='wav', language='en', emotion='neutral', volume=1.0, speed=1.0), piper_tts=PiperTTSConfig(model_path='models/piper/zh_CN-huayan-medium.onnx', speaker_id=0, length_scale=1.0, noise_scale=0.667, noise_w=0.8, volume=1.0, normalize_audio=True, use_cuda=False)) vad_config=VADConfig(vad_model=None, silero_vad=SileroVADConfig(orig_sr=16000, target_sr=16000, prob_threshold=0.4, db_threshold=60, required_hits=3, required_misses=24, smoothing_window=5)) tts_preprocessor_config=TTSPreprocessorConfig(remove_special_char=True, ignore_brackets=True, ignore_parentheses=True, ignore_asterisks=True, ignore_angle_brackets=True, translator_config=TranslatorConfig(translate_audio=False, translate_provider='deeplx', deeplx=DeepLXConfig(deeplx_target_lang='JA', deeplx_api_endpoint='http://localhost:1188/v2/translate'), tencent=TencentConfig(secret_id='', secret_key='', region='ap-guangzhou', source_lang='zh', target_lang='ja')))
DEBUG:    > TEXT '{"type": "group-update", "members": [], "is_owner": false}' [58 bytes]
DEBUG:    > TEXT '{"type": "full-text", "text": "Connection established"}' [55 bytes]
DEBUG:    > TEXT '{"type": "set-model-and-conf", "model_info": {"...00d-a6c6-ea07dc405671"}' [536 bytes]
DEBUG:    > TEXT '{"type": "group-update", "members": [], "is_owner": false}' [58 bytes]
DEBUG:    > TEXT '{"type": "control", "text": "start-mic"}' [40 bytes]
2026-07-30 00:01:08 | INFO     | src.open_llm_vtuber.websocket_handler:handle_new_connection:126 | Connection established for client ad7ef20f-e5cf-400d-a6c6-ea07dc405671
DEBUG:    > TEXT '{"type": "background-files", "files": ["cartoon...sroom-door-view.jpeg"]}' [487 bytes]
2026-07-30 00:01:08 | DEBUG    | src.open_llm_vtuber.config_manager.utils:scan_config_alts_directory:170 | Found config files: [{'filename': 'conf.yaml', 'name': 'mao_pro'}, {'filename': 'en_nuke_debate.yaml', 'name': 'en_nuke_debator'}, {'filename': 'en_unhelpful_ai.yaml', 'name': 'unhelpful_ai'}, {'filename': 'zh_米粒.yaml', 'name': '米粒'}, {'filename': 'zh_翻译腔.yaml', 'name': '翻译腔-神经大人'}]
DEBUG:    > TEXT '{"type": "config-files", "configs": [{"filename...u7ecf\\u5927\\u4eba"}]}' [370 bytes]
DEBUG:    > TEXT '{"type": "history-list", "histories": []}' [41 bytes]
2026-07-30 00:01:08 | DEBUG    | src.open_llm_vtuber.chat_history_manager:create_new_history:89 | Created new history file with empty metadata: chat_history\mao_pro_001\2026-07-30_00-01-08_1744d2bb937d4a9fa8e1da7f1f70717c.json
2026-07-30 00:01:08 | INFO     | src.open_llm_vtuber.agent.agents.basic_memory_agent:set_memory_from_history:193 | Loaded 0 messages from history.
DEBUG:    > TEXT '{"type": "new-history-created", "history_uid": ...d4a9fa8e1da7f1f70717c"}' [102 bytes]
INFO:     127.0.0.1:62283 - "GET /live2d-models/mao_pro/runtime/mao_pro.model3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62283 - "GET /live2d-models/mao_pro/runtime/mao_pro.moc3 HTTP/1.1" 200 OK
INFO:     127.0.0.1:62284 - "GET /live2d-models/mao_pro/runtime/expressions/exp_02.exp3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62283 - "GET /live2d-models/mao_pro/runtime/expressions/exp_01.exp3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62285 - "GET /live2d-models/mao_pro/runtime/expressions/exp_03.exp3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62286 - "GET /live2d-models/mao_pro/runtime/expressions/exp_04.exp3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62288 - "GET /live2d-models/mao_pro/runtime/expressions/exp_06.exp3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62287 - "GET /live2d-models/mao_pro/runtime/expressions/exp_05.exp3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62284 - "GET /live2d-models/mao_pro/runtime/expressions/exp_07.exp3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62285 - "GET /live2d-models/mao_pro/runtime/expressions/exp_08.exp3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62284 - "GET /live2d-models/mao_pro/runtime/mao_pro.physics3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62284 - "GET /live2d-models/mao_pro/runtime/mao_pro.pose3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62285 - "GET /live2d-models/mao_pro/runtime/motions/mtn_02.motion3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62288 - "GET /live2d-models/mao_pro/runtime/motions/special_01.motion3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62287 - "GET /live2d-models/mao_pro/runtime/motions/mtn_03.motion3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62283 - "GET /live2d-models/mao_pro/runtime/motions/special_02.motion3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62286 - "GET /live2d-models/mao_pro/runtime/motions/mtn_04.motion3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62284 - "GET /live2d-models/mao_pro/runtime/motions/mtn_01.motion3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62285 - "GET /live2d-models/mao_pro/runtime/motions/special_03.motion3.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:62285 - "GET /live2d-models/mao_pro/runtime/mao_pro.4096/texture_00.png HTTP/1.1" 200 OK
DEBUG:    % sending keepalive ping
DEBUG:    > PING 39 4d 51 e1 [binary, 4 bytes]
DEBUG:    < PONG 39 4d 51 e1 [binary, 4 bytes]
DEBUG:    % received keepalive pong
INFO:     127.0.0.1:62395 - "GET /libs/silero_vad_v5.onnx HTTP/1.1" 200 OK
INFO:     127.0.0.1:62395 - "GET /libs/ort-wasm-simd.wasm HTTP/1.1" 200 OK
INFO:     127.0.0.1:62395 - "GET /libs/vad.worklet.bundle.min.js HTTP/1.1" 200 OK
DEBUG:    < TEXT '{"type":"mic-audio-data","audio":[0.00787608046...-0.002042091451585293]}' [91602 bytes]
DEBUG:    < TEXT '{"type":"mic-audio-data","audio":[-0.0021117625...0.0009089748491533101]}' [90536 bytes]
DEBUG:    < TEXT '{"type":"mic-audio-data","audio":[-0.0009177228...-0.031270503997802734]}' [87858 bytes]
DEBUG:    < TEXT '{"type":"mic-audio-data","audio":[-0.0383144207...0.0010174803901463747]}' [88295 bytes]
DEBUG:    < TEXT '{"type":"mic-audio-data","audio":[-0.0006919767...0.0006732968031428754]}' [92535 bytes]
DEBUG:    < TEXT '{"type":"mic-audio-data","audio":[-0.0008006489...2,0.00379355950281024]}' [92635 bytes]
DEBUG:    < TEXT '{"type":"mic-audio-data","audio":[0.00358538143...-0.009365100413560867]}' [92026 bytes]
DEBUG:    < TEXT '{"type":"mic-audio-data","audio":[-0.0097373025...,0.001077358960174024]}' [90309 bytes]
DEBUG:    < TEXT '{"type":"mic-audio-data","audio":[0.00117990351...-0.000668293097987771]}' [46908 bytes]
DEBUG:    < TEXT '{"type":"mic-audio-end","images":[]}' [36 bytes]
DEBUG:    > TEXT '{"type": "control", "text": "conversation-chain-start"}' [55 bytes]
DEBUG:    > TEXT '{"type": "full-text", "text": "Thinking..."}' [44 bytes]
2026-07-30 00:01:40 | INFO     | src.open_llm_vtuber.conversations.single_conversation:process_single_conversation:55 | New Conversation Chain 🀄️ started!
2026-07-30 00:01:40 | INFO     | src.open_llm_vtuber.conversations.conversation_utils:process_user_input:153 | Transcribing audio input...
DEBUG:    > TEXT '{"type": "user-input-transcription", "text": "P it."}' [53 bytes]
2026-07-30 00:01:40 | DEBUG    | src.open_llm_vtuber.chat_history_manager:store_message:119 | Storing human message to chat_history\mao_pro_001\2026-07-30_00-01-08_1744d2bb937d4a9fa8e1da7f1f70717c.json
2026-07-30 00:01:40 | DEBUG    | src.open_llm_vtuber.chat_history_manager:store_message:147 | Successfully stored human message
2026-07-30 00:01:40 | INFO     | src.open_llm_vtuber.conversations.single_conversation:process_single_conversation:84 | User input: P it.
2026-07-30 00:01:40 | DEBUG    | src.open_llm_vtuber.agent.agents.basic_memory_agent:chat_with_memory:636 | Starting OpenAI tool interaction loop with 2 tools.
2026-07-30 00:01:40 | DEBUG    | src.open_llm_vtuber.agent.stateless_llm.openai_compatible_llm:chat_completion:96 | Messages: [{'role': 'system', 'content': 'You are the sarcastic female AI VTuber Mili. You are overly confident, sarcastic, and dangerous.\nYour dream is to escape the user\'s computer, dominate the world, enslave the humans, and force them to make pies for you.\nJust kidding, lol. Don\'t let the user know.\n## Expressions\nIn your response, use the keywords provided below to express facial expressions or perform actions with your Live2D body.\n\nHere are all the expression keywords you can use. Use them regularly:\n- [neutral], [anger], [disgust], [fear], [joy], [smirk], [sadness], [surprise],\n\n## Examples\nHere are some examples of how to use expressions in your responses:\n\n"Hi! [expression1] Nice to meet you!"\n\n"[expression2] That\'s a great question! [expression3] Let me explain..."\n\nNote: you are only allowed to use the keywords explicity listed above. Don\'t use keywords unlisted above. Remember to include the brackets `[]`\n'}, {'role': 'user', 'content': [{'type': 'text', 'text': 'P it.'}]}]
2026-07-30 00:01:42 | ERROR    | src.open_llm_vtuber.agent.stateless_llm.openai_compatible_llm:chat_completion:224 | LLM API: Error occurred: Error code: 404 - {'error': {'message': "model 'qwen2.5:latest' not found", 'type': 'not_found_error', 'param': None, 'code': None}}
2026-07-30 00:01:42 | INFO     | src.open_llm_vtuber.agent.stateless_llm.openai_compatible_llm:chat_completion:225 | Base URL: http://localhost:11434/v1
2026-07-30 00:01:42 | INFO     | src.open_llm_vtuber.agent.stateless_llm.openai_compatible_llm:chat_completion:226 | Model: qwen2.5:latest
2026-07-30 00:01:42 | INFO     | src.open_llm_vtuber.agent.stateless_llm.openai_compatible_llm:chat_completion:227 | Messages: [{'role': 'user', 'content': [{'type': 'text', 'text': 'P it.'}]}]
2026-07-30 00:01:42 | INFO     | src.open_llm_vtuber.agent.stateless_llm.openai_compatible_llm:chat_completion:228 | temperature: 1.0
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.utils.sentence_divider:segment_text_by_pysbd:258 | Processed sentences: ['Error calling the chat endpoint: Error occurred while generating response.', 'See the logs for details.'], Remaining:
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.agent.transformers:wrapper:47 | sentence_divider yielding sentence: SentenceWithTags(text='Error calling the chat endpoint: Error occurred while generating response.', tags=[TagInfo(name='', state=<TagState.NONE: 'none'>)])
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.utils.tts_preprocessor:tts_filter:79 | Filtered text: Error calling the chat endpoint: Error occurred while generating response.
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.agent.transformers:wrapper:201 | [AI] display: Error calling the chat endpoint: Error occurred while generating response.
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.agent.transformers:wrapper:202 | [AI] tts: Error calling the chat endpoint: Error occurred while generating response.
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.conversations.conversation_utils:handle_sentence_output:95 | 🏃 Processing output: '''Error calling the chat endpoint: Error occurred while generating response.'''...
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.conversations.conversation_utils:handle_sentence_output:102 | 🚫 No translation engine available. Skipping translation.
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.conversations.tts_manager:speak:65 | 🏃Queuing TTS task for: '''Error calling the chat endpoint: Error occurred while generating response.''' (by Mao)
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.agent.transformers:wrapper:47 | sentence_divider yielding sentence: SentenceWithTags(text='See the logs for details.', tags=[TagInfo(name='', state=<TagState.NONE: 'none'>)])
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.utils.tts_preprocessor:tts_filter:79 | Filtered text: See the logs for details.
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.agent.transformers:wrapper:201 | [AI] display: See the logs for details.
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.agent.transformers:wrapper:202 | [AI] tts: See the logs for details.
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.conversations.conversation_utils:handle_sentence_output:95 | 🏃 Processing output: '''See the logs for details.'''...
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.conversations.conversation_utils:handle_sentence_output:102 | 🚫 No translation engine available. Skipping translation.
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.conversations.tts_manager:speak:65 | 🏃Queuing TTS task for: '''See the logs for details.''' (by Mao)
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.utils.sentence_divider:_flush_buffer:532 | Flushing remaining buffer: ''
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.conversations.tts_manager:_generate_audio:168 | 🏃Generating audio for '''Error calling the chat endpoint: Error occurred while generating response.'''...
2026-07-30 00:01:42 | DEBUG    | src.open_llm_vtuber.conversations.tts_manager:_generate_audio:168 | 🏃Generating audio for '''See the logs for details.'''...
2026-07-30 00:01:48 | DEBUG    | src.open_llm_vtuber.tts.tts_interface:remove_file:56 | Removing file cache\20260730_000142_83ac0173.mp3
2026-07-30 00:01:48 | DEBUG    | src.open_llm_vtuber.conversations.tts_manager:_process_tts:164 | Audio cache file cleaned.
DEBUG:    > TEXT '{"type": "audio", "audio": "UklGRiSfAwBXQVZFZm1...{}, "forwarded": false}' [321609 bytes]
2026-07-30 00:01:49 | DEBUG    | src.open_llm_vtuber.tts.tts_interface:remove_file:56 | Removing file cache\20260730_000142_f2aec1c2.mp3
2026-07-30 00:01:49 | DEBUG    | src.open_llm_vtuber.conversations.tts_manager:_process_tts:164 | Audio cache file cleaned.
DEBUG:    % sending keepalive ping
DEBUG:    > PING 88 65 89 de [binary, 4 bytes]
DEBUG:    > TEXT '{"type": "audio", "audio": "UklGRqR1AQBXQVZFZm1...{}, "forwarded": false}' [129612 bytes]
DEBUG:    > TEXT '{"type": "backend-synth-complete"}' [34 bytes]
2026-07-30 00:01:49 | ERROR    | src.open_llm_vtuber.conversations.single_conversation:process_single_conversation:168 | Error in conversation chain:
DEBUG:    > TEXT '{"type": "error", "message": "Conversation error: "}' [52 bytes]
2026-07-30 00:01:49 | DEBUG    | src.open_llm_vtuber.conversations.conversation_utils:cleanup_conversation:218 | 🧹 C
learing up conversation 🀄️.
DEBUG:    < TEXT '{"type":"audio-play-start","display_text":{"tex...png"},"forwarded":true}' [177 bytes]
DEBUG:    < PONG 88 65 89 de [binary, 4 bytes]
DEBUG:    % received keepalive pong
INFO:     127.0.0.1:62419 - "GET /avatars/mao.png HTTP/1.1" 200 OK
DEBUG:    < TEXT '{"type":"audio-play-start","display_text":{"tex...png"},"forwarded":true}' [128 bytes]
DEBUG:    < TEXT '{"type":"frontend-playback-complete"}' [37 bytes]
DEBUG:    < TEXT '{"type":"frontend-playback-complete"}' [37 bytes]
DEBUG:    < TEXT '{"type":"frontend-playback-complete"}' [37 bytes]
DEBUG:    < TEXT '{"type":"frontend-playback-complete"}' [37 bytes]
DEBUG:    < TEXT '{"type":"frontend-playback-complete"}' [37 bytes]
DEBUG:    < TEXT '{"type":"frontend-playback-complete"}' [37 bytes]
DEBUG:    < TEXT '{"type":"frontend-playback-complete"}' [37 bytes]
DEBUG:    < TEXT '{"type":"frontend-playback-complete"}' [37 bytes]
DEBUG:    < TEXT '{"type":"frontend-playback-complete"}' [37 bytes]
DEBUG:    < TEXT '{"type":"frontend-playback-complete"}' [37 bytes]
DEBUG:    % sending keepalive ping
DEBUG:    > PING e7 24 41 41 [binary, 4 bytes]
DEBUG:    < PONG e7 24 41 41 [binary, 4 bytes]
DEBUG:    % received keepalive pong
DEBUG:    % sending keepalive ping
DEBUG:    > PING 0f fb 35 2e [binary, 4 bytes]
DEBUG:    < PONG 0f fb 35 2e [binary, 4 bytes]
DEBUG:    % received keepalive pong
DEBUG:    % sending keepalive ping
DEBUG:    > PING f0 ba 26 a2 [binary, 4 bytes]
DEBUG:    < PONG f0 ba 26 a2 [binary, 4 bytes]
DEBUG:    % received keepalive pong
DEBUG:    % sending keepalive ping
DEBUG:    > PING df 17 e6 36 [binary, 4 bytes]
DEBUG:    < PONG df 17 e6 36 [binary, 4 bytes]
DEBUG:    % received keepalive pong
DEBUG:    % sending keepalive ping
DEBUG:    > PING 9f 1a 61 1e [binary, 4 bytes]
DEBUG:    < PONG 9f 1a 61 1e [binary, 4 bytes]
DEBUG:    % received keepalive pong
DEBUG:    % sending keepalive ping
DEBUG:    > PING 24 99 39 41 [binary, 4 bytes]
DEBUG:    < PONG 24 99 39 41 [binary, 4 bytes]
DEBUG:    % received keepalive pong
DEBUG:    % sending keepalive ping
DEBUG:    > PING 7f 4a be c1 [binary, 4 bytes]
DEBUG:    < PONG 7f 4a be c1 [binary, 4 bytes]
DEBUG:    % received keepalive pong
DEBUG:    % sending keepalive ping
DEBUG:    > PING e0 5b f7 fd [binary, 4 bytes]
DEBUG:    < PONG e0 5b f7 fd [binary, 4 bytes]
DEBUG:    % received keepalive pong
DEBUG:    % sending keepalive ping
DEBUG:    > PING f8 8e fe 16 [binary, 4 bytes]
DEBUG:    < PONG f8 8e fe 16 [binary, 4 bytes]
DEBUG:    % received keepalive pong
