import subprocess
import logging
import platform
from litestar import Litestar, Response
from litestar.openapi import OpenAPIConfig
from litestar.exceptions import NotFoundException

from .routers import retrieve_offerwall, get_offer_names
from .config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

openapi_config = OpenAPIConfig(
    title="OfferWalls API",
    version="1",
    description="API for work with OfferWalls and Offers",
)


def handle_not_found(request, exc: NotFoundException) -> Response:
    return Response(content={"detail": exc.detail}, status_code=404)


app = Litestar(
    route_handlers=[retrieve_offerwall, get_offer_names],
    openapi_config=openapi_config,
    exception_handlers={NotFoundException: handle_not_found},
)


if __name__ == "__main__":
    logger.info("Starting Granian on http://%s:%s", settings.host, settings.port)
    logger.info("OpenAPI docs: http://%s:%s/schema", settings.host, settings.port)

    if platform.system() == "Windows":
        subprocess.run(
            [
                "python",
                "-m",
                "granian",
                "--interface",
                "asgi",
                "app.__main__:app",
                "--host",
                settings.host,
                "--port",
                str(settings.port),
            ],
            check=True,
        )
    else:
        subprocess.run(
            [
                "granian",
                "--interface",
                "asgi",
                "app.__main__:app",
                "--host",
                settings.host,
                "--port",
                str(settings.port),
            ],
            check=True,
        )