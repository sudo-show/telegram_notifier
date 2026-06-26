# telegram-notifier

A lightweight asynchronous wrapper around python-telegram-bot for sending Telegram notifications.

The package provides automatic retries for Telegram rate limits and network timeouts while keeping the API minimal.

## Features

* Async API
* Automatic retry on Telegram rate limits (RetryAfter)
* Automatic retry on request timeouts (TimedOut)
* Supports HTML message formatting
* Optional silent notifications
* Simple, dependency-light interface

## Installation

```pip install telegram-notifier```

## Quick Start

```
import asyncio
from telegram_notifier import Notifier
async def main():
    notifier = Notifier(
        token="YOUR_BOT_TOKEN",
        channel="@your_channel",
    )
    await notifier.notify("Hello from <b>telegram-notifier</b>!")
asyncio.run(main())
```

Parameters:

* message – Message text (HTML formatting is supported).
* silent – Send without notification sound.
* retries – Number of retry attempts for rate limits and timeouts.

## Error Handling

The notifier automatically retries when:

* Telegram responds with a rate limit (RetryAfter)
* A request times out (TimedOut)

Unexpected exceptions are logged and re-raised.

## Requirements

* Python 3.10+
* python-telegram-bot