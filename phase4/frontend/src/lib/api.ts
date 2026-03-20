import axios from "axios";

const getApiBaseURL = () => {
    if (typeof window !== "undefined") return "/api/proxy";
    return process.env.API_URL || "http://backend-service:8000";
};

// Create Axios client pointed to FastAPI backend
export const api = axios.create({
    baseURL: getApiBaseURL(),
    withCredentials: true, // Auto-attaches BetterAuth HttpOnly cookies
});

export const sendChatMessage = async (userId: string, message: string, conversationId?: number) => {
    const response = await api.post(`/api/${userId}/chat`, { message, conversation_id: conversationId });
    return response.data;
};
