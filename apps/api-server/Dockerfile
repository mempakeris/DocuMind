FROM ghcr.io/astral-sh/uv:python3.13-alpine

RUN addgroup -S -g 2000 nonroot \
 && adduser -S -u 2000 -G nonroot -h /home/nonroot nonroot
USER nonroot

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY --chown=nonroot:nonroot . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

ENV PATH="/app/.venv/bin:$PATH"