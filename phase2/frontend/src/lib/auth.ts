import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";

import { Pool } from "pg";

export const auth = betterAuth({
    emailAndPassword: {
        enabled: true,
    },
    // Connecting BetterAuth directly to the Neon Serverless Postgres DB
    database: new Pool({ connectionString: process.env.DATABASE_URL || process.env.CONNECTION_STRING || "postgres://dummy:pw@localhost/db" }),
    plugins: [
        jwt()
    ],
    secret: process.env.BETTER_AUTH_SECRET || "supersecret-dev-key"
});
