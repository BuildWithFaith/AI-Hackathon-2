"use client";

import { useState, useRef, useEffect } from "react";
import { Send, User, Bot, Trash, Sparkles } from "lucide-react";
import { useSession } from "@/lib/auth-client";
import { sendChatMessage } from "@/lib/api";

export default function ChatPage() {
  const { data: session, isPending } = useSession();
  const [messages, setMessages] = useState<{ id: number; role: "user" | "assistant"; content: string }[]>([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [conversationId, setConversationId] = useState<number | undefined>(undefined);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || !session?.user?.id) return;

    const userMsg = input.trim();
    setInput("");
    setMessages((prev) => [...prev, { id: Date.now(), role: "user", content: userMsg }]);
    setIsLoading(true);

    try {
      const result = await sendChatMessage(session.user.id, userMsg, conversationId);
      setConversationId(result.conversation_id);
      setMessages((prev) => [...prev, { id: Date.now(), role: "assistant", content: result.response }]);
    } catch (error) {
      console.error("Chat error:", error);
      setMessages((prev) => [...prev, { id: Date.now(), role: "assistant", content: "Sorry, there was an error processing your request." }]);
    } finally {
      setIsLoading(false);
    }
  };

  if (isPending) return <div className="min-h-screen flex items-center justify-center bg-zinc-950 text-white">Loading...</div>;
  if (!session) return <div className="min-h-screen flex items-center justify-center bg-zinc-950 text-white">Please sign in to use the AI Chatbot. <a href="/" className="ml-2 text-indigo-400">Go Home</a></div>;

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-950 via-slate-900 to-black flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-3xl flex-1 max-h-[90vh] flex flex-col glassmorphic-panel rounded-3xl overflow-hidden border border-white/10 shadow-2xl bg-white/5 backdrop-blur-xl">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-white/10 bg-black/40">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-indigo-500/20 rounded-xl">
              <Sparkles className="w-6 h-6 text-indigo-300" />
            </div>
            <div>
              <h1 className="text-xl font-bold text-white">AI Todo Assistant</h1>
              <p className="text-indigo-200/80 text-sm">Natural Language Task Management</p>
            </div>
          </div>
          <button 
            onClick={() => { setMessages([]); setConversationId(undefined); }}
            className="p-2 text-indigo-300 hover:text-white hover:bg-white/10 rounded-xl transition-colors"
            title="Clear Chat"
          >
            <Trash className="w-5 h-5" />
          </button>
        </div>

        {/* Messages List */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          {messages.length === 0 ? (
            <div className="flex flex-col items-center justify-center h-full text-indigo-200/60 opacity-80">
              <div className="w-20 h-20 rounded-full bg-indigo-500/10 flex items-center justify-center mb-6 border border-indigo-500/20">
                <Bot className="w-10 h-10 text-indigo-400" />
              </div>
              <p className="text-lg">Send a message to start managing your tasks!</p>
              <p className="text-sm mt-3 bg-white/5 px-4 py-2 rounded-full border border-white/5">Try: "Add a task to buy groceries" or "What's pending?"</p>
            </div>
          ) : (
            messages.map((m) => (
              <div key={m.id} className={`flex gap-4 ${m.role === "user" ? "justify-end" : "justify-start"}`}>
                {m.role === "assistant" && (
                  <div className="w-8 h-8 rounded-full bg-indigo-500/20 flex items-center justify-center flex-shrink-0 border border-indigo-500/30 shadow-lg shadow-indigo-500/20">
                    <Bot className="w-4 h-4 text-indigo-300" />
                  </div>
                )}
                <div className={`max-w-[80%] p-4 text-[15px] leading-relaxed backdrop-blur-md shadow-xl ${m.role === "user" ? "bg-indigo-600 text-white rounded-2xl rounded-tr-sm shadow-indigo-600/20" : "bg-white/10 text-indigo-50 rounded-2xl rounded-tl-sm border border-white/10"}`}>
                  <p className="whitespace-pre-wrap">{m.content}</p>
                </div>
                {m.role === "user" && (
                  <div className="w-8 h-8 rounded-full bg-black/20 flex items-center justify-center flex-shrink-0 border border-white/10">
                    <User className="w-4 h-4 text-indigo-300" />
                  </div>
                )}
              </div>
            ))
          )}
          {isLoading && (
            <div className="flex gap-4 justify-start">
              <div className="w-8 h-8 rounded-full bg-indigo-500/20 flex items-center justify-center flex-shrink-0 border border-indigo-500/30">
                <Bot className="w-4 h-4 text-indigo-300" />
              </div>
              <div className="max-w-[80%] p-4 rounded-2xl backdrop-blur-md bg-white/10 text-indigo-100 rounded-tl-sm border border-white/10 shadow-xl">
                <div className="flex gap-1.5 items-center h-5">
                  <div className="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-bounce" style={{ animationDelay: '0ms' }} />
                  <div className="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-bounce" style={{ animationDelay: '150ms' }} />
                  <div className="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-bounce" style={{ animationDelay: '300ms' }} />
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <div className="p-4 bg-black/40 border-t border-white/10">
          <form onSubmit={handleSubmit} className="flex gap-3">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type your command (e.g., 'Reschedule my meeting')..."
              className="flex-1 bg-white/5 border border-white/10 rounded-2xl px-5 py-3.5 text-white placeholder-indigo-200/40 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 transition-all font-light"
              disabled={isLoading}
            />
            <button
              type="submit"
              disabled={isLoading || !input.trim()}
              className="bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 disabled:hover:bg-indigo-600 text-white p-3.5 rounded-2xl transition-colors shadow-lg shadow-indigo-500/20 flex items-center justify-center"
            >
              <Send className="w-5 h-5 -ml-0.5" />
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
