# Litestar OfferWalls Microservice

## Implemented Features
1. **Litestar Microservice**
   - Endpoints:
     - `GET /api/offerwalls/{token}` — retrieve an OfferWall by token.
     - `GET /api/offerwalls/get_offer_names/` — get a list of all available offer names.
   - Automatic OpenAPI documentation available at `/schema`.
   - Asynchronous interaction with PostgreSQL database.

2. **Docker**
   - Separate `Dockerfile` for the Litestar microservice.
   - `docker-compose.yml` for running Litestar, PostgreSQL, and Nginx.
   - Django admin panel temporarily **disabled** to allow testing the microservice independently.

3. **Nginx**
   - Proxying `/api/` and `/schema` to Litestar.
   - Static files and media served via aliases.

4. **Testing**
   - `curl http://localhost:5000/api/offerwalls/get_offer_names/` returns the list of all offers (status 200).
   - `GET /api/offerwalls/{token}` returns 404 for a non-existent token.

**Author:** Anton Podolian  
**Branch:** `feat/litestar-microservice`

