import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        # Sign in
        res = await client.post("http://localhost:3000/api/auth/sign-in/email", json={
            "email": "testuser@example.com",
            "password": "password123"
        })
        cookies = client.cookies
        
        # Create a task
        res_create = await client.post("http://localhost:8000/api/tasks", json={
            "title": "Test Task",
            "description": "Test Desc"
        }, cookies=cookies)
        task = res_create.json()
        print("Created:", task)
        
        # Mark as complete
        task_id = task["id"]
        res_patch = await client.patch(f"http://localhost:8000/api/tasks/{task_id}/complete", cookies=cookies)
        print("Patched:", res_patch.json())
        
        # Fetch again
        res_get = await client.get("http://localhost:8000/api/tasks", cookies=cookies)
        tasks = res_get.json()
        print("Fetched completed status:", [t["completed"] for t in tasks if t["id"] == task_id])

asyncio.run(main())
