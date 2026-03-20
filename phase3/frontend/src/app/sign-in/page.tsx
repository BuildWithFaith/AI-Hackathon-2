"use client";
import { useState } from "react";
import { signIn } from "@/lib/auth-client";
import { useRouter } from "next/navigation";

export default function SignIn() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const router = useRouter();

    const handleSignIn = async (e: React.FormEvent) => {
        e.preventDefault();
        const { data, error } = await signIn.email({
            email,
            password,
        });
        if (error) {
            alert(error.message);
        } else {
            router.push("/");
        }
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
            <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-md">
                <h1 className="text-2xl font-bold mb-6 text-center text-gray-800">Sign In to Tasks</h1>
                <form onSubmit={handleSignIn} className="space-y-4">
                    <input
                        type="email"
                        placeholder="Email"
                        value={email}
                        onChange={e => setEmail(e.target.value)}
                        className="w-full text-black p-2 border border-gray-300 rounded focus:border-blue-500 focus:outline-none"
                        required
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={e => setPassword(e.target.value)}
                        className="w-full p-2 border border-gray-300 rounded focus:border-blue-500 focus:outline-none text-black"
                        required
                    />
                    <button type="submit" className="w-full py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition font-medium">
                        Sign In
                    </button>
                </form>
                <div className="mt-4 text-center">
                    <a href="/sign-up" className="text-blue-500 hover:text-blue-600 hover:underline">Don't have an account? Sign Up</a>
                </div>
            </div>
        </div>
    );
}
