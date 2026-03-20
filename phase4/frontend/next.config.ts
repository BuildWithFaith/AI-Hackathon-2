import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  async rewrites() {
    return [
      {
        source: "/api/proxy/:path*",
        destination: `http://backend-service:8000/:path*`,
      },
      {
        source: "/api/proxy",
        destination: `http://backend-service:8000`,
      }
    ];
  },
};

export default nextConfig;
