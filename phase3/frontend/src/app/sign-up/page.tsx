"use client";
import { useState } from "react";
import { signUp } from "@/lib/auth-client";
import { useRouter } from "next/navigation";

export default function SignUp() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [name, setName] = useState("");
    const router = useRouter();

    const handleSignUp = async (e: React.FormEvent) => {
        e.preventDefault();
        const { data, error } = await signUp.email({
            email,
            password,
            name,
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
                <h1 className="text-2xl font-bold mb-6 text-center text-gray-800">Create an Account</h1>
                <form onSubmit={handleSignUp} className="space-y-4">
                    <input
                        type="text"
                        placeholder="Full Name"
                        value={name}
                        onChange={e => setName(e.target.value)}
                        className="w-full p-2 border border-gray-300 rounded focus:border-blue-500 focus:outline-none"
                        required
                    />
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
                        className="w-full p-2 border border-gray-300 text-black rounded focus:border-blue-500 focus:outline-none"
                        required
                    />
                    <button type="submit" className="w-full py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition font-medium">
                        Sign Up
                    </button>
                </form>
                <div className="mt-4 text-center">
                    <a href="/sign-in" className="text-blue-500 hover:text-blue-600 hover:underline">Already have an account? Sign In</a>
                </div>
            </div>
        </div>
    );
}
