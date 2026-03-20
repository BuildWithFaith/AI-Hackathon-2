import axios from "axios";

// Create Axios client pointed to FastAPI backend
export const api = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",
    withCredentials: true, // Auto-attaches BetterAuth HttpOnly cookies
});

export const sendChatMessage = async (userId: string, message: string, conversationId?: number) => {
    const response = await api.post(`/api/${userId}/chat`, { message, conversation_id: conversationId });
    return response.data;
};
