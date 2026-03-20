"use client";

import { useEffect, useState } from "react";
import { api } from "@/lib/api";
import { useSession, signOut } from "@/lib/auth-client";
import { useRouter } from "next/navigation";
import { LogOut, CheckCircle2, Circle, Trash2, Plus } from "lucide-react";

interface Task {
    id: number;
    title: string;
    description: string | null;
    completed: boolean;
}

export default function Dashboard() {
    const { data: session, isPending } = useSession();
    const router = useRouter();
    const [tasks, setTasks] = useState<Task[]>([]);
    const [title, setTitle] = useState("");
    const [filter, setFilter] = useState("all");
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (!isPending && !session) {
            router.push("/sign-in");
        } else if (session) {
            fetchTasks(filter);
        }
    }, [session?.user?.id, isPending, filter]);

    const fetchTasks = async (statusFilter = "all") => {
        try {
            setLoading(true);
            const { data } = await api.get(`/api/tasks?status=${statusFilter}`);
            setTasks(data);
        } catch (error) {
            console.error("Failed to fetch tasks", error);
        } finally {
            setLoading(false);
        }
    };

    const handleCreateTask = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!title.trim()) return;
        try {
            const { data } = await api.post("/api/tasks", { title });
            setTasks(prev => [...prev, data]);
            setTitle("");
        } catch (error) {
            console.error("Failed to create task", error);
        }
    };

    const toggleComplete = async (taskId: number) => {
        try {
            // Optimistically update UI so it doesn't wait 2 seconds
            setTasks(prev => prev.map(t => t.id === taskId ? { ...t, completed: !t.completed } : t));
            await api.patch(`/api/tasks/${taskId}/complete`);
        } catch (error) {
            // Revert on failure
            setTasks(prev => prev.map(t => t.id === taskId ? { ...t, completed: !t.completed } : t));
            console.error("Failed to update task", error);
        }
    };

    const deleteTask = async (taskId: number) => {
        try {
            setTasks(prev => prev.filter(t => t.id !== taskId));
            await api.delete(`/api/tasks/${taskId}`);
        } catch (error: any) {
            if (error?.response?.status !== 404) {
               console.error("Failed to delete task", error);
            }
        }
    };

    const handleSignOut = async () => {
        await signOut();
        router.push("/sign-in");
    };

    if (isPending) return <div className="flex h-screen items-center justify-center">Loading...</div>;
    if (!session) return null;

    return (
        <div className="min-h-screen bg-gray-50 p-8">
            <div className="max-w-3xl mx-auto bg-white rounded-xl shadow-sm p-6">
                <div className="flex justify-between items-center mb-8 border-b pb-4">
                    <h1 className="text-3xl font-bold text-gray-800">My Tasks</h1>
                    <div className="flex items-center gap-4">
                        <span className="text-gray-600 font-medium">Hello, {session.user.name}</span>
                        <button onClick={handleSignOut} className="text-gray-500 hover:text-red-500 flex items-center gap-1 transition">
                            <LogOut size={18} /> Sign Out
                        </button>
                    </div>
                </div>

                <form onSubmit={handleCreateTask} className="flex gap-2 mb-6">
                    <input
                        type="text"
                        value={title}
                        onChange={e => setTitle(e.target.value)}
                        placeholder="What needs to be done?"
                        className="flex-1 p-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition shadow-sm text-black"
                    />
                    <button type="submit" className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 flex items-center gap-2 font-medium shadow-sm transition">
                        <Plus size={20} /> Add
                    </button>
                </form>

                <div className="flex gap-2 mb-6 bg-gray-100 p-1 rounded-lg w-max">
                    {['all', 'pending', 'completed'].map(f => (
                        <button
                            key={f}
                            onClick={() => setFilter(f)}
                            className={`px-4 py-1.5 rounded-md capitalize font-medium transition ${filter === f ? 'bg-white text-blue-600 shadow-sm' : 'text-gray-500 hover:text-gray-800'}`}
                        >
                            {f}
                        </button>
                    ))}
                </div>

                {loading ? (
                    <div className="text-center text-gray-500 py-12">
                        <div className="animate-pulse flex flex-col items-center">
                            <div className="h-4 bg-gray-200 rounded w-1/4 mb-4"></div>
                            <div className="h-4 bg-gray-200 rounded w-1/2"></div>
                        </div>
                    </div>
                ) : tasks.length === 0 ? (
                    <div className="text-center text-gray-500 py-12 bg-gray-50 rounded-lg border border-dashed border-gray-200">
                        No tasks found. Create one above!
                    </div>
                ) : (
                    <div className="space-y-3">
                        {tasks.map(task => (
                            <div key={task.id} className={`flex items-center justify-between p-4 rounded-lg border ${task.completed ? 'bg-gray-50 border-gray-100' : 'bg-white border-gray-200 hover:border-blue-300'} transition cursor-pointer shadow-sm`}>
                                <div className="flex items-center gap-3 flex-1" onClick={() => toggleComplete(task.id)}>
                                    <button className={`${task.completed ? 'text-green-500' : 'text-gray-300 hover:text-blue-500'} transition`}>
                                        {task.completed ? <CheckCircle2 size={24} /> : <Circle size={24} />}
                                    </button>
                                    <span className={`${task.completed ? 'line-through text-gray-400' : 'text-gray-800 font-medium'} transition`}>
                                        {task.title}
                                    </span>
                                </div>
                                <button onClick={() => deleteTask(task.id)} className="text-gray-400 hover:text-red-500 p-2 transition ml-4">
                                    <Trash2 size={18} />
                                </button>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}
