import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "Executive Intelligence AI", description: "A connected workspace for executive operations and business intelligence." };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="en"><body>{children}</body></html>; }
