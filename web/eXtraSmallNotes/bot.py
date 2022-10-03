import asyncio
import os
from playwright.async_api import async_playwright

with open('flag.txt') as fp:
    FLAG = fp.read()

NOTEPAD_URL = os.getenv('NOTEPAD_URL', 'http://localhost:8000')
BOT_HOST = os.getenv('BOT_HOST', '0.0.0.0')
BOT_PORT = os.getenv('BOT_PORT', '8001')


async def handle(browser, reader, writer):
    writer.write(b'Waiting for URL\n')
    await writer.drain()

    url = await reader.read(1000)
    if not (url.startswith(b'http://') or url.startswith(b'https://')):
        writer.write(b'Invalid Scheme')
        await writer.drain()
    else:
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(NOTEPAD_URL)
        await page.fill('#add_note_content', FLAG)
        await page.click('#add_note_button')
        await page.goto('about:blank')
        await page.goto(url.decode(), wait_until="domcontentloaded")
        await asyncio.sleep(30)
        await page.close()
        writer.write(b'Done')
        await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main():
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=True)

        server = await asyncio.start_server(lambda r, w: handle(browser, r, w), BOT_HOST, BOT_PORT)

        async with server:
            await server.serve_forever()


asyncio.run(main())
