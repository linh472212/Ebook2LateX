# Gọi thư viện FastAPI
from fastapi import FastAPI

# Tạo đối tượng app từ class FastAPI
app = FastAPI()

# Tạo decorator cho đường dẫn gốc
@app.get("/")
def read_root():
    return {"message": "Chao mung ban den voi Ebook2LateX!"}