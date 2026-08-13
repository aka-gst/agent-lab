• План выполнен без изменений файлов.

  1. Определить корень checkout, ветку, состояние Git и submodule.
  2. Проследить серверный путь до conversation flow.
  3. Найти фабрики Agent/LLM/ASR/TTS и соответствующие схемы.
  4. Проверить OpenAI-compatible клиент и оценить возможность PoC.
  5. Инвентаризировать frontend и CI.

  ## Атомарная цель

  Составить локальную архитектурную карту Open-LLM-VTuber и определить, можно ли подключить первый PoC через
  существующий OpenAI-compatible provider без рефакторинга.

  ## Состояние checkout

  - Корень: C:\dev\agent-lab\Open-LLM-VTuber
  - Ветка: feat/local-agent-gateway
  - Это не main.
  - git status --short: пустой, рабочее дерево чистое.
  - Файлы не изменялись.
  - Frontend инициализирован как submodule на commit 06a659b114fff788cf0daaa86e484576db4975bf.

  ## Карта и входные точки

  run_server.py
    └─ WebSocketServer
        ├─ FastAPI app
        ├─ routes.py
        │   ├─ /client-ws
        │   ├─ /proxy-ws
        │   ├─ web-tool HTTP routes
        │   └─ /tts-ws
        ├─ ServiceContext
        │   ├─ ASRFactory
        │   ├─ TTSFactory
        │   └─ AgentFactory
        │       └─ StatelessLLMFactory
        │           └─ OpenAI-compatible AsyncLLM
        └─ frontend/ static mount

  /client-ws
    └─ WebSocketHandler
        └─ handle_conversation_trigger
            ├─ process_single_conversation
            │   └─ ASR → agent.chat() → output processing → TTS
            └─ process_group_conversation
                └─ ASR → member agents → output processing → TTS

  ### Server

  - Главная исполняемая точка: Open-LLM-VTuber/run_server.py:119
      - читает и валидирует conf.yaml;
      - создаёт WebSocketServer;
      - вызывает асинхронную инициализацию;
      - запускает Uvicorn.

  - FastAPI application: Open-LLM-VTuber/src/open_llm_vtuber/server.py:56
      - регистрирует routers;
      - монтирует cache, Live2D, backgrounds, avatars, web tool и frontend;
      - frontend монтируется последним как /.

  ### Routes

  - Все backend routes: Open-LLM-VTuber/src/open_llm_vtuber/routes.py:15
  - Основной клиентский WebSocket: /client-ws.
  - Опциональный proxy WebSocket: /proxy-ws.
  - Отдельный TTS WebSocket: /tts-ws.
  - Здесь же находятся web-tool redirects и HTTP endpoints для ресурсов.

  ### Service context

  - Центр сборки runtime-зависимостей: Open-LLM-VTuber/src/open_llm_vtuber/service_context.py:41
  - Создаёт и хранит:
      - asr_engine;
      - tts_engine;
      - vad_engine;
      - agent_engine;
      - Live2D, translation и MCP-компоненты.

  - Фабричные вызовы:
      - ASR — строка 326;
      - TTS — строка 338;
      - Agent — строка 382.

  ### Conversation flow

  - Маршрутизация WebSocket-сообщений: Open-LLM-VTuber/src/open_llm_vtuber/websocket_handler.py:61
  - mic-audio-end, text-input и ai-speak-signal ведут в _handle_conversation_trigger.
  - Выбор одиночного или группового сценария: Open-LLM-VTuber/src/open_llm_vtuber/conversations/
    conversation_handler.py:19

  - Одиночный диалог: Open-LLM-VTuber/src/open_llm_vtuber/conversations/single_conversation.py:25
      - process_user_input;
      - context.agent_engine.chat;
      - process_agent_output;
      - TTS и WebSocket output.

  - Групповой диалог: Open-LLM-VTuber/src/open_llm_vtuber/conversations/group_conversation.py:29
  - Общие преобразования ASR/output: Open-LLM-VTuber/src/open_llm_vtuber/conversations/conversation_utils.py:45
  - Очередь и генерация TTS: Open-LLM-VTuber/src/open_llm_vtuber/conversations/tts_manager.py:16
  - Типы и group state: Open-LLM-VTuber/src/open_llm_vtuber/conversations/types.py:12

  ### Agent factory

  - Open-LLM-VTuber/src/open_llm_vtuber/agent/agent_factory.py:15
  - Выбирает basic_memory_agent, mem0_agent, hume_ai_agent или letta_agent.
  - Для basic_memory_agent извлекает llm_provider, берёт его конфигурацию и вызывает stateless factory.

  ### Stateless LLM factory

  - Open-LLM-VTuber/src/open_llm_vtuber/agent/stateless_llm_factory.py:14
  - openai_compatible_llm и несколько специализированных OpenAI-compatible профилей направляются в один
    OpenAICompatibleLLM.

  - Также поддерживает template, Ollama, llama.cpp и Claude реализации.

  ### OpenAI-compatible client

  - Open-LLM-VTuber/src/open_llm_vtuber/agent/stateless_llm/openai_compatible_llm.py:24
  - Использует официальный AsyncOpenAI.
  - Передаёт base_url, api_key, organization, project, model и temperature.
  - Делает streaming-вызов client.chat.completions.create(..., stream=True).
  - Поддерживает OpenAI tool-call schema.
  - При распознанной ошибке “does not support tools” отключает tools для последующих запросов.

  ### Config schemas

  Главный граф схем:

  - Open-LLM-VTuber/src/open_llm_vtuber/config_manager/main.py:11
  - Open-LLM-VTuber/src/open_llm_vtuber/config_manager/system.py:7
  - Open-LLM-VTuber/src/open_llm_vtuber/config_manager/character.py:13
  - Open-LLM-VTuber/src/open_llm_vtuber/config_manager/agent.py:14
  - Open-LLM-VTuber/src/open_llm_vtuber/config_manager/stateless_llm.py:58
  - Open-LLM-VTuber/src/open_llm_vtuber/config_manager/asr.py:310
  - Open-LLM-VTuber/src/open_llm_vtuber/config_manager/tts.py:683
  - Open-LLM-VTuber/src/open_llm_vtuber/config_manager/vad.py:41
  - Open-LLM-VTuber/src/open_llm_vtuber/config_manager/tts_preprocessor.py:100
  - Default example: Open-LLM-VTuber/config_templates/conf.default.yaml:58

  OpenAICompatibleConfig требует base_url, llm_api_key и model; organization_id и project_id опциональны.

  ### ASR

  - Factory: Open-LLM-VTuber/src/open_llm_vtuber/asr/asr_factory.py:5
  - Interface: Open-LLM-VTuber/src/open_llm_vtuber/asr/asr_interface.py
  - Реализации находятся в src/open_llm_vtuber/asr/:
      - Faster Whisper;
      - whisper.cpp;
      - OpenAI Whisper;
      - FunASR;
      - Azure;
      - Groq Whisper;
      - Sherpa ONNX.

  ### TTS

  - Factory: Open-LLM-VTuber/src/open_llm_vtuber/tts/tts_factory.py:5
  - Interface: Open-LLM-VTuber/src/open_llm_vtuber/tts/tts_interface.py
  - Реализации находятся в src/open_llm_vtuber/tts/.
  - Отдельно уже имеется OpenAI-compatible TTS:
      - Open-LLM-VTuber/src/open_llm_vtuber/tts/openai_tts.py:18
      - схема OpenAITTSConfig в config_manager/tts.py.

  ### Frontend submodule

  - Path: Open-LLM-VTuber/frontend
  - Declaration: Open-LLM-VTuber/.gitmodules
  - Upstream: Open-LLM-VTuber/Open-LLM-VTuber-Web
  - Отслеживаемая ветка submodule: build
  - Checkout содержит собранные index.html, JS/CSS assets, Live2D и VAD runtime assets.

  ### CI

  Каталог: Open-LLM-VTuber/.github/workflows

  - ruff.yml — Ruff на push и pull request.
  - codeql.yml — CodeQL на push, PR и по расписанию.
  - update-requirements.yml — регенерация requirements через uv.
  - docker-blacksmith.yml — multi-architecture Docker build/push.
  - create_release.yml — release packages, модели и desktop installers.
  - fossa_scan.yml — dependency/license scan.

  ## Можно ли сделать PoC без refactor?

  Да, первый PoC можно выполнить без рефакторинга, только через существующий openai_compatible_llm.

  Минимальная конфигурационная цепочка уже существует:

  basic_memory_agent.llm_provider = openai_compatible_llm
  llm_configs.openai_compatible_llm:
    base_url
    llm_api_key
    model
    temperature

  Это сработает, если gateway/provider реализует достаточно совместимый POST /chat/completions, включая streaming-ответы
  OpenAI SDK. Для простого текстового PoC tools можно не использовать. Если нужны MCP/tool calls, endpoint должен
  корректно поддерживать streaming tool-call deltas; автоматическое отключение tools покрывает только определённый класс
  явных ошибок.

  Это вывод из статического чтения, а не runtime-доказательство: я не читал рабочий conf.yaml, поскольку он может
  содержать ключи, и не обращался к реальному provider endpoint.

  ## Риски и предположения

  - Совместимость заявленного OpenAI API может не включать streaming или точную структуру chunks.
  - Пользовательский conf.yaml не проверялся и не выводился.
  - Инициализация полного ServiceContext может потребовать настроенные ASR/TTS и локальные модели.
  - CI содержит lint/security/build workflows, но отдельного unit-test workflow в найденном наборе нет.
  - Первая команда была запущена уровнем выше Git-корня и честно вернула not a git repository.
  - Один rg завершился кодом 1 из-за Windows glob-синтаксиса; соответствующие запросы были повторены корректно и
    завершились кодом 0.

  ## Команды проверки для будущего PoC

  Без изменения кода минимально релевантны:

  uv run ruff check src/open_llm_vtuber/agent src/open_llm_vtuber/config_manager
  uv run python -c "from src.open_llm_vtuber.config_manager import Config; print('imports-ok')"
  uv run run_server.py --verbose

  Последняя команда докажет загрузку реального конфига и инициализацию контекста, но сама по себе не докажет успешный
  LLM round trip. Для этого потребуется один реальный запрос через /client-ws.

  Следующий шаг: отдельно согласовать атомарный read-only smoke test OpenAI-compatible endpoint без печати ключей и без
  изменения файлов.

─ Worked for 3m 03s 