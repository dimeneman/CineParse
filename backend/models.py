from typing import Optional
from pydantic import BaseModel, Field


class MovieInformation(BaseModel):
    movie_name: Optional[str] = Field(
        default=None,
        description="Name of the movie"
    )

    genre: Optional[str] = Field(
        default=None,
        description="Genre of the movie"
    )

    director: Optional[str] = Field(
        default=None,
        description="Director of the movie"
    )

    cast: list[str] = Field(
        default_factory=list,
        description="Main cast members"
    )

    rating: Optional[str] = Field(
        default=None,
        description="Movie rating"
    )

    runtime: Optional[str] = Field(
        default=None,
        description="Runtime of the movie"
    )

    language: Optional[str] = Field(
        default=None,
        description="Language"
    )

    short_summary: Optional[str] = Field(
        default=None,
        description="Short summary"
    )