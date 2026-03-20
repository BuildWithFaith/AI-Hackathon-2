from fastapi import Request, HTTPException
import httpx
import os

async def get_current_user_id(request: Request, secret_key: str = None) -> str:
    auth_header = request.headers.get("Authorization")
    token = None
    
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        
    if not token:
        # BetterAuth plugins often secure session string inside https standard cookies
        token = request.cookies.get("better-auth.session_token") or request.cookies.get("__Secure-better-auth.session_token")
        
    if not token:
        raise HTTPException(status_code=401, detail="Missing or invalid authentication token")
    
    # Send request to Next.js Better Auth endpoint to verify session
    headers = {
        "cookie": f"better-auth.session_token={token}"
    }
    
    app_url = os.getenv("NEXT_PUBLIC_APP_URL", "http://localhost:3000")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{app_url}/api/auth/get-session", headers=headers)
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Error contacting auth server: {str(e)}")
            
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid session token")
        
    data = response.json()
    if not data or not data.get("session") or not data.get("user"):
        raise HTTPException(status_code=401, detail="Invalid session data returned from auth server")
        
    user_id = data["user"].get("id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Token payload missing user identifier")
        
    return user_id

