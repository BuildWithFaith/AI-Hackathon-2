import axios from "axios";

// Create Axios client pointed to FastAPI backend
export const api = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",
    withCredentials: true, // Auto-attaches BetterAuth HttpOnly cookies
});
