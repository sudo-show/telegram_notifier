import asyncio
import logging
import os
from datetime import timedelta
from telegram import Bot
from telegram.error import RetryAfter, TimedOut


class Notifier:
    def __init__(self, channel: str, token: str):
        self.logger = logging.getLogger(__name__)
        self.channel: str = channel
        self.bot = Bot(token=token)

    async def notify(
        self,
        message: str,
        silent: bool = False,
        retries: int = 3,
    ) -> None:
        for _ in range(retries):
            try:
                await self.bot.send_message(
                    chat_id=self.channel,
                    text=message,
                    parse_mode="HTML",
                    disable_notification=silent,
                )
                return

            except RetryAfter as e:
                if isinstance(e.retry_after, timedelta):
                    wait_time = int(e.retry_after.total_seconds()) + 1
                else:
                    wait_time = e.retry_after + 1

                self.logger.warning(f"Telegram rate limit hit. Retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)

            except TimedOut:
                self.logger.warning("Telegram timed out. Retrying in 2s...")
                await asyncio.sleep(2)

            except Exception:
                self.logger.exception("Failed to send Telegram notification.")
                raise

        self.logger.error("Telegram notification failed after all retries.")