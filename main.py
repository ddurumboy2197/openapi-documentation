from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Muvaffaqiyatli API",
    description="Muvaffaqiyatli API uchun ochiq API tafsilotlari",
    version="1.0",
    contact={
        "name": "Muvaffaqiyatli API",
        "url": "https://example.com",
        "email": "support@muvaffaqiyatli-api.com"
    },
    license={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    }
)

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users/", response_model=list[User])
async def get_users():
    return [
        User(id=1, name="John Doe", email="john@example.com"),
        User(id=2, name="Jane Doe", email="jane@example.com")
    ]

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    return User(id=user_id, name="John Doe", email="john@example.com")
```

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

```bash
curl http://localhost:8000/docs
```

```bash
curl http://localhost:8000/openapi.json
