import httpx
import asyncio
import json

async def main():
    async with httpx.AsyncClient() as client:
        # 1. Sign in to better-auth
        print("Signing in...")
        # We need a user. Let's just create one or use a dummy one.
        # Acutally let's register a user first.
        try:
            res_up = await client.post("http://localhost:3000/api/auth/sign-up/email", json={
                "email": "testuser@example.com",
                "password": "password123",
                "name": "Test User"
            })
            print("Sign up status:", res_up.status_code)
            print("Sign up response:", res_up.text)
        except Exception as e:
            print("Sign up error:", e)

        res = await client.post("http://localhost:3000/api/auth/sign-in/email", json={
            "email": "testuser@example.com",
            "password": "password123"
        })
        print("Sign in status:", res.status_code)
        print("Cookies:", client.cookies)
        
        # 2. Try reaching the backend
        print("\nSending request to backend...")
        res_backend = await client.get("http://localhost:8000/api/tasks", cookies=client.cookies)
        print("Backend status:", res_backend.status_code)
        print("Backend response:", res_backend.text)
        
        # Also print the token exactly
        token = client.cookies.get("better-auth.session_token")
        if token:
            print("\nToken obtained:", token[:20], "...")
            import jwt
            try:
                decoded = jwt.decode(token, "supersecret-dev-key", algorithms=["HS256"], options={"verify_aud": False})
                print("Decoded Token Data:", decoded)
            except Exception as e:
                print("PyJWT Decode Error:", e)
        else:
            print("No token in cookies.")

if __name__ == "__main__":
    asyncio.run(main())
