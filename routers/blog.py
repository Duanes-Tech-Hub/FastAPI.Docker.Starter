from fastapi import APIRouter
from model.BlogData import BlogData

router = APIRouter(
    prefix="/api/v1/blog",
    tags=["blog"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_blogs():
    return {
                [
                    {
                        "id": 1,
                        "title": "Blog Name One",
                        "description": "A description about the blog.",
                        "tags": "General",
                        "url": "/api/v1/blog/blog-slug-one",
                        "author": "John Doe"
                    },
                    {
                        "id": 2,
                        "title": "Blog Name Two",
                        "description": "A description about the blog.",
                        "tags": "General",
                        "url": "/api/v1/blog/blog-slug-two",
                        "author": "Mary Smith"
                    }
                ]
            }

@router.get("/{blog_id}")
async def get_blog(blog_id: int):
    return {"message": f" Return specific blog based on ID: {blog_id} "}

@router.post("/blog")
async def create_blog(blog: BlogData):
    return {"message": "Blog created successfully", "blog": blog}