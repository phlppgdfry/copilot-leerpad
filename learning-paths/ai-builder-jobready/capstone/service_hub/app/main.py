"""Training API: intentionally not suitable for production or personal data."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .db import connect, initialize


class TicketCreate(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    description: str = Field(min_length=5, max_length=2000)
    category: Literal["question", "incident", "request"] = "question"


def create_app(db_path: str | None = None) -> FastAPI:
    database_path = db_path or os.environ.get(
        "SERVICE_HUB_DB_PATH", str(Path("data") / "servicehub.db")
    )
    initialize(database_path)
    app = FastAPI(title="Service Operations Hub (training only)")

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/tickets", status_code=201)
    def create_ticket(payload: TicketCreate) -> dict[str, object]:
        with connect(database_path) as connection:
            cursor = connection.execute(
                "INSERT INTO tickets (title, description, category) VALUES (?, ?, ?)",
                (payload.title, payload.description, payload.category),
            )
            row = connection.execute(
                "SELECT * FROM tickets WHERE id = ?", (cursor.lastrowid,)
            ).fetchone()
        assert row is not None
        return dict(row)

    @app.get("/tickets")
    def list_tickets() -> list[dict[str, object]]:
        with connect(database_path) as connection:
            rows = connection.execute(
                "SELECT * FROM tickets ORDER BY id DESC"
            ).fetchall()
        return [dict(row) for row in rows]

    @app.get("/tickets/{ticket_id}")
    def get_ticket(ticket_id: int) -> dict[str, object]:
        with connect(database_path) as connection:
            row = connection.execute(
                "SELECT * FROM tickets WHERE id = ?", (ticket_id,)
            ).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Ticket not found")
        return dict(row)

    return app


app = create_app()
