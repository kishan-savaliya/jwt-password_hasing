import uvicorn

if __name__ == '__main__':
    uvicorn.run("app.app:user", host = 'localhost', port = 8000, reload=True)
