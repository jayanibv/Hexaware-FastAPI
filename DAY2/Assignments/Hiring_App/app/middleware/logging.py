import time


class LoggingMiddleware:

    def __init__(self, app):
        self.app = app


    async def __call__(self, scope, receive, send):

        if scope["type"] == "http":

            start = time.time()

            async def send_wrapper(message):

                if message["type"] == "http.response.start":

                    duration = time.time() - start

                    print(
                        f"{scope['method']} {scope['path']} "
                        f"{duration:.4f}s"
                    )

                await send(message)

            await self.app(scope, receive, send_wrapper)

        else:
            await self.app(scope, receive, send)