from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    preferences: dict | None = None
    created_at: str


class TaskCreate(BaseModel):
    title: str
    # description: str | None = None
    # status: str | None = "backlog"
    # complexity: str | None = "medium"


class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    complexity: str
    ai_tip: str | None = None
    owner_id: int
    created_at: str


class TaskUpdate(BaseModel):
    title: str | None = None
    status: str | None = None
    complexity: str | None = None
    ai_tip: str | None = None
