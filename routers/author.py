from fastapi import APIRouter
from model.AuthorData import AuthorData

router = APIRouter(
    prefix="/api/v1/author",
    tags=["author"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_authors():
    return {
                [
                    {
                        "id": 1,
                        "firstname": "John",
                        "lastname": "Doe",
                        "description": "A brief description about John.",
                        "email": "john.doe@example.com",
                        "website": "https://johndoe.com"
                    },
                    {
                        "id": 2,
                        "firstname": "Mary",
                        "lastname": "Smith",
                        "description": "A brief description about Mary.",
                        "email": "mary.smith@example.com",
                        "website": "https://marysmith.com"
                    }
                ]
            }

@router.get("/{author_id}")
async def get_author(author_id: int):
    return {"message": f" Return specific author based on ID: {author_id} "}

@router.post("/author")
async def create_author(author: AuthorData):
    return {"message": "Author created successfully", "author": author}